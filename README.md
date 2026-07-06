# 西班牙语词根词缀体系地图 · Mapa Etimológico

以 **A-Z 字母 + 词根/词缀 + 拉丁词源** 为线索的西班牙语词汇体系地图。把单词按首字母索引，用拉丁化+拉丁语源+形态拆解（前缀+词根+后缀）+ 历史音变 + 跨语言同源，帮初学者建立「音→形→义→源」的系统记忆。

姊妹项目：韩语 (`../Korean/`) / 日语 (`../Japanese/`)，同架构、同交互。

## 设计思想（源自两份提示词文档）

1. **A-Z 音·形·义地图**：每字母含三层——史源（腓尼基/拉丁原型）、音感（发音动作）、字形意象
2. **拉丁→西语音变规则**（= 韩语「造物主矩阵」）：f→h、ĕ→ie、ŏ→ue、pl/cl/fl→ll、-ct→ch、双拉丁词
3. **词根/前缀/后缀三层拆解**：`re- + con- + struct- + -ción`，详情卡彩色可视化
4. **词族语义树 + 跨语言同源**：拉丁起点 → 西/英/法/意 cognate 对比
5. **20 大类语义标签**（两级结构「一级 > 二级」，强制归一）

## 索引规则

- 按单词**实际首字母**索引：`helado`→H、`gelatina`→G
- `hel-`/`gel-` 共享拉丁源 `gelatus`，作为**词源关联**展示（不混索引）
- 后缀（如 `-ado`）按首字母索引（A），标注 `sufijo` 类型

## 种子词族（gel-/hel-：寒冷、凝固）

拉丁 `gelatus`（冻结的）经 **g→h 音变** → 西语 `hel-` 家族；保留 g 形式的 `gel-` 多为后期书面借词。

| 单词 | 词根 | 拉丁源 | 释义 |
|---|---|---|---|
| helado | hel- | gelatus | 🍦冰淇淋 |
| helar | hel- | gelare | ❄️结冰 |
| helada | hel- | gelata | 🌫️霜冻 |
| hielo | hel- | gelus | 🧊冰 |
| heladero | hel- | — | 🍧冰淇淋商 |
| gelatina | gel- | gelatina | 🍮明胶（保留g，后期借词）|
| -ado | — | -atus | 📎过去分词后缀 |

另含 am-/amor（爱）、luc-/luz（光）、dic-/decir（说）、struct-（建造：reconstrucción）等词族。

## 功能（同韩/日语项目）

- **A-Z 字母导图**（按发音部位分组：Vocales/Bilabiales/Dentales/Velares...）
- **3-pane**：词根列表 | 词条 | 详情（形态拆解可视化 + 词源 + cognates）
- **AI 双配置**：主 LLM（新词条，深度词源分析）+ 补全 LLM（批量填充）
- **AI 释义 emoji**（呼应词根义）
- **多端同步**（GitHub Gist）+ PWA + 本地 CORS 代理
- **20 大类语义标签**（两级，强制归一，防语法污染）
- **移动端**字号优化、清搜清签、双击联动、最近添加抽屉

## 使用

1. 直接打开 `spanish_etymology_map.html`
2. ⚙ 设置 → 填 LLM API Key（推荐 GLM-4.5 / DeepSeek / Claude）
3. 点 ✨ AI 新词条，输入 `helado` 或 `冰淇淋` → AI 自动拆解词根/词源/cognate

## 文件

- `spanish_etymology_map.html` — 单文件应用
- `manifest.json` / `sw.js` — PWA
- `glm_proxy.py` — 本地 CORS 代理（解决浏览器跨域）

## 提示词参考

教学框架源自 `西班牙语学习提示词+A到Z音形义地图+字母群音群词素示例.md`（24 维分析）与 `西班牙语提示词（ChatGPT生成）.txt`（A-Z 音形义地图 + 音群词素）。
