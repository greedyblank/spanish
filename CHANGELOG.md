# 更新记录 · CHANGELOG

## 西1 — 初始版本（2026-07-06）

基于韩语/日语姊妹项目架构，构建西班牙语词根词缀体系地图：

- **A-Z 字母导图**：27 字母按发音部位分组（Vocales/Bilabiales/Dentales/Velares/Palatales/Fricativas/Líquidas/Raras），每字母含史源/音感/字形意象三层（源自腓尼基/拉丁原型）
- **拉丁→西语音变规则矩阵**（= 韩语造物主矩阵）：f→h、ĕ→ie、ŏ→ue、pl/cl/fl→ll、-ct→ch、双拉丁词（通俗继承 vs 书面借词）
- **3-pane 导航**：词根列表 | 词条列表 | 详情面板，highlight/filter 解耦模型
- **形态拆解可视化**：详情卡把 breakdown 拆成彩色语素（前缀琥珀/词根蓝/后缀绿），如 `re- + con- + struct- + -ción`
- **20 大类语义标签**（两级「一级 > 二级」，强制归一，防语法污染）
- **AI 双配置**：主 LLM 深度词源分析（拉丁语源/音变/cognate/词族）+ 补全 LLM 批量字段
- **AI 释义 emoji**（呼应词根义）
- **多端同步**（GitHub Gist）+ PWA + 本地 CORS 代理
- **种子数据**：gel-/hel- 词族（helado/helar/helada/hielo/heladero/gelatina/-ado）+ am-/amor、luc-/luz、dic-/decir、struct-（reconstrucción）共 12 词条

**索引规则**：按单词实际首字母索引（helado→H，gelatina→G），hel-/gel- 共享拉丁源 gelatus 作为词源关联展示。
