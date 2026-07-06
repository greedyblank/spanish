# 更新记录 · CHANGELOG

## 西3 — 6 项特性补全（参考韩/日）（2026-07-06）

- **词根释义带 emoji**（#8）：种子 rootMeaning 加 emoji 前缀（hel-→❄️寒冷、凝固；am-→❤️爱；luz→💡光）；AI 新词条 prompt 引导 rootMeaning 开头带 1-2 emoji。
- **POS 适用性过滤**（#9）：`FIELD_APPLICABILITY`（gender→名词/代词/数词/形容词；verbClass/regularity→动词）+ `_isFieldApplicable`；`applyCompletions` 硬过滤，AI 不会给动词填 gender、给名词填 verbClass。
- **补全字段分组全选**（#12）：内容/分类/词法三组各有全选/全不选 + `setGroupFields`。
- **标签浏览器 collapseAll**（#13）：`collapseAllTagTree` + 头部「▿ 全收缩」按钮。
- **AI 标签重组**（#11）：完整实现（参考韩语）——`collectTagsForAI`/`buildTagRestructurePrompt`/`showTagRestructurePreview`（6 步清洗）/`retryMissingTagsAI`（仅补漏）+ 应用预览弹窗。
- **双击联动核对**（#10）：确认 highlight/filter 解耦——单击词根只高亮不筛选，切到词根详情面板；默认全量显示。

## 西2 — 参考韩日项目完善（中文化+语法字段+词根详情面板）（2026-07-06）

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
