#!/usr/bin/env python3
"""
本地 CORS 代理 — 解决浏览器无法直接调用 GLM/DeepSeek/Moonshot/OpenAI/Anthropic 等 API 的跨域问题。

【用法】
  1. 终端运行：  python3 glm_proxy.py
  2. 在 spanish_etymology_map.html 的 ⚙ 设置中勾选「使用本地代理」
  3. 端点保持原样（如 https://open.bigmodel.cn/api/anthropic/v1/messages）
  4. 重新点 ✨ AI 补全 → 🔗 测试连接

【停止】Ctrl+C
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.error
import json
import sys

PORT = 8787

class CORSProxy(BaseHTTPRequestHandler):
    def _send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        self.send_header('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, x-api-key, anthropic-version, '
                         'anthropic-dangerous-direct-browser-access, Accept')
        self.send_header('Access-Control-Max-Age', '86400')

    def do_OPTIONS(self):
        self.send_response(204); self._send_cors(); self.end_headers()

    def do_POST(self):
        target = self.path.lstrip('/')
        if not target.startswith('http'):
            target = 'https://' + target
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length > 0 else b''
        fwd_headers = {'Content-Type': self.headers.get('Content-Type', 'application/json')}
        for h in ('Authorization', 'x-api-key', 'anthropic-version', 'anthropic-dangerous-direct-browser-access', 'Accept'):
            v = self.headers.get(h)
            if v: fwd_headers[h] = v
        req = urllib.request.Request(target, data=body, headers=fwd_headers, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = resp.read()
                self.send_response(resp.status)
                ct = resp.headers.get('Content-Type', 'application/json')
                self.send_header('Content-Type', ct); self._send_cors(); self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self.send_header('Content-Type', 'application/json; charset=utf-8'); self._send_cors(); self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(502)
            self.send_header('Content-Type', 'application/json; charset=utf-8'); self._send_cors(); self.end_headers()
            self.wfile.write(json.dumps({'error':'proxy_error','message':str(e),'hint':'检查目标 URL 与 API Key'}, ensure_ascii=False).encode())

    def log_message(self, fmt, *args):
        msg = fmt % args
        color = '\033[91m' if ('404' in msg or '502' in msg or '500' in msg) else '\033[92m'
        sys.stderr.write(f"{color}[{self.log_date_time_string()}] {msg}\033[0m\n")

if __name__ == '__main__':
    print(f"""\033[95m╔══════════════════════════════════════════════════════════╗
║  🚀 Spanish LLM CORS Proxy 已启动                         ║
║  监听: http://localhost:{PORT}                              ║
╚══════════════════════════════════════════════════════════╝\033[0m

\033[90m按 Ctrl+C 停止代理\033[0m""")
    try:
        HTTPServer(('127.0.0.1', PORT), CORSProxy).serve_forever()
    except KeyboardInterrupt:
        print('\n\033[93m代理已停止\033[0m'); sys.exit(0)
