# 更新记录 · CHANGELOG

## 西7 — 同源词/标签云/交互/补全（24 项）（2026-07-11）

- **同源词 COGNADOS 重做**（#1/#1-1/#1-2/#1-3）：改为药丸样式（对标 FAMILIA）、语言名用 2 字缩写（意/法/葡/英…）、每条同源词带发音+释义（修复 bug：不再只有第一条有）、每条后加小播放按钮 `playButton('xs', langCode)`。保留 `englishCognate` 斜杠串一眼总览。
- **播放按钮扩展**（#2/#5）：派生词族每词后加小播放按钮、例句每行后加播放按钮（读西语句子部分）。
- **形态拆解缩小**（#4）：语素 pill padding/size 均减小（`2px 8px`→`1px 6px`，font-size 0.85em）。
- **导航历史全局返回**（#2）：header 增加 `← 返回` 按钮。`selectEntry/selectRoot/dblClickRoot/dblClickEntry/selectLetter/onTagClick/jumpToMorpheme` 等核心导航均推入 `_navHistory` 栈（最大 60），点返回逐级回退（恢复 letter/filter/tag/highlight/selected 全状态）。历史空时按钮变暗不可点。
- **双击词条不切详情**（#6）：`dblClickEntry` 只高亮+定位词根到左栏（`highlightRoot`），**详情保持显示当前双击的单词**，不切到词根详情（与之前 #8 语义对照：单击词根→词根详情；双击词根→第一个词详情）。双击词条=词条详情+词根高亮；双击词根=词条详情+词根高亮。
- **字母分组筛选重构**（#8）：进入字母组 = 展示「首字母=该字母的词条」或「任一词根/词缀在该组的词条」（`_letterGroupIds`/`_inLetterGroup`）。`仅词根` 模式下额外过滤：词表只展示由该组**词根**派生的词；`仅词缀` 同理。
- **标签云改为语义标签云**（#3/#3-1/#3-2/#3-3/#3-4/#3-5）：PCIC 官方 20 大类标记🔷；`tagCloudState.selectedSubTag` 支持二级精确筛选（点一级→展开二级+全量词条；点二级→只看该二级词条）；词表/标签筛选联动；浏览器整行可点击展开（不限于三角）；一级→二级箭头颜色改为 `#34d399` 醒目；新增「🧹 清除空组」按钮。
- **AI 补全双 Tab**（#10）：全量补全弹窗分 **「📝 单词补全」/「🌱 词根/词缀补全」**，Tab 切换联动 `_completionTab`+`findIncompleteEntries` 过滤。从词根详情进→自动切 roots Tab 并默认去勾 gender/verbClass（不适用字段）。
- **AI 补全取消`仅填空字段`后可用**（#7）：取消勾选不再禁用「开始补全」按钮——屏幕提示改为含警告「将覆盖全部 N 条」，用户自主决定覆盖。
- **新建词条自动创建缺失词根条目**（#9）：`saveEntry` 后调用 `_createRootStub` 为 `root`+`roots[]` 中每个被引用但无条目的词根/词缀快速建 stub（含推断的 rootMeaning/latinOrigin），后续可用 AI 补全充实。
- **前缀/后缀徽章差异化**（#11）：`.prefix-badge`（橙色）vs `.suffix-badge`（绿色），与词根 `.root-badge`（蓝色）一眼区分。词根列表的 affix 项 + 详情卡均使用。
- **词缀排序忽略前导 `-`**（#12）：`_sortKey` 剥离前导 `-`，`getVisibleEntries` 统一使用。
- **重音符号指引**（#1）：AI 新词条 prompt 明示 `á é í ó ú ñ` 规则、疑问词 vs 关系代词的重音区分、IPA 重音标注。
- **种子/数据补全**：`_LANG_ORDER` 语言缩写映射、`playButton` 支持 `lang` 参数按语言 TTS、`speak` 支持 `lang` 参数、`groupedCognates` 修复 englishCognate 兜底逻辑（只补 cognates[] 未出现的，不覆盖已有发音释义）。

## 西6 — 本地文件实时同步 + 数据自愈工具（2026-07-11）

- **绑定本地文件（File System Access API）**：移植自韩/日姊妹项目。设置里「📁 绑定本地」选一个 `.json` 后，每次修改自动写盘（600ms 防抖），句柄存 IndexedDB 跨会话保留（`restoreFileSync`），刷新后自动恢复。搜索栏上方有同步状态指示条（已绑定显示文件名+时间+解绑；未绑定显示「绑定」入口）。仅 Chrome/Edge 支持，不支持时指示条自动隐藏。与 Gist 多端同步**并存不冲突**（`save()` 里两条并列）。写盘格式 = 导出格式（entries/tagGraph/tombstones/version），可直接被「↑ 导入」读回。
  - 用途：防清浏览器缓存丢数据；本地始终有一份最新 json（便于外部工具/AI 读改）。
  - **注意**：本地导入（↑ 导入）是**整体覆盖**（`state.entries = d.entries`），不合并、不解决冲突；导入前建议先导出留底。带按 id 合并 + 墓碑的冲突解决只在 Gist 同步路径（`mergeState`）。
- **数据自愈 `repairData`（0 token，纯本地）**：新增「🧹 整理修复」按钮（设置里）。拆分组合词根（`luc-/luz`→主根+`roots[]`）、为被引用但无自身条目的词根/词缀建立真实条目、重建 PCIC 两级标签结构去语法污染。默认不自动跑（避免打扰），仅手动触发。修复本身不调 LLM。

## 西5 — 词根成真实条目 / 删除级联 / 同源词分组 / 12 项打磨（2026-07-11）

- **词根/词缀成为真实条目**（模型/#3）：pos 为 词根/前缀/后缀 的条目有自己独立的释义·分析·词源·同源词。词根详情一律取「自身条目」(`findRootEntry`)，**绝不再借用第一个派生词**——修复了「bien-/ven- 显示成 bienvenido 的语义」的 bug。主词条列表默认隐藏词根/词缀条目（`showRootEntries` 开关，「词根条目」按钮切换）。无独立条目的词根显示⚠提示 +「建立词根条目」按钮。详见 ADR 0005。
- **删除词根/词缀级联**（#4）：词缀=弱关联（属性），删除只解除关联、绝不删词；词根=强关联，删除时仅挂靠它的「孤儿」词移入「⌀ 暂无词根挂靠」分组（不删词），多词根词只解除该关联。新增 **AI 重新挂靠**：为孤儿词判断应归入哪个现有词根，无匹配则提议新建（需勾选确认，不自动建）。详见 ADR 0006。
- **搜索后点词根跳转修复**（#0）：双击词根跳转时，落到「当前过滤后可见列表」里的第一个词，而非全局第一个（避免跳到不在列表里的词）。
- **圆形播放按钮**（#1）：▶ 外套圆圈描边，词条列表 + 详情统一 `playButton`。
- **补全/重组 token 审查**（#2）：确认补全 prompt **本就只带勾选字段**（非全量）；重组 prompt 把 tagGraph 整张 pretty-JSON 改为紧凑「子→父」父链，省 token。词根/词缀详情也接入编辑/补全/删除。
- **词缀补全用固有含义**（#3）：补全 prompt 识别词根/词缀条目，强制描述其「跨所有派生词通用」的固有含义/构词作用，而非某个所在词的意思。
- **词汇列表显示发音**（#7）：IPA 紧跟词汇后，属性徽章在发音后。
- **同源词按语言分组 + 每条发音释义**（#8）：保留 `englishCognate` 斜杠串一眼总览；`cognates` 数组 `{lang,word,ipa,meaning}` 允许同语言多条，渲染按语言分组、英语优先（`renderCognatesBlock`）。
- **详情属性标签改真 pill**（#5）：阴阳性等从 `[中括号]` 文本改为真正的 pill 徽章。
- **多词根不建组合词根**（#6）：种子 `luc-/luz`、`dic-/dec-` 拆成 主词根 + `roots[]`；AI prompt 明令禁止 `luc-/luz`、`bien-ven` 这类拼接词根。
- **标签浏览器两级 + 联动**（#9）：确认 PCIC 一级 > 二级 父子结构；补全/新词条/重组 prompt 均强制二级挂官方一级；标签云/浏览器与三栏联动正常。
- **返回键保留选中**（#10）：返回只清字母筛选，保留选中词条 + 高亮词根。
- **多词根反向关联校验**（#11）：双击词条固定反向到主词根（`getRootKey`=`e.root`）；双击词根/词缀条目本身反向到自己。

## 西4 — 发音系统 / 多词根 / PCIC 分类 / 交互重构（2026-07-10）

- **发音标注系统**（#1）：新增 `ipa`（国际音标）+ `pronNote`（发音说明：重音/特殊字母/西美差异）两字段。详情卡新增「发音 Pronunciación」区；新增/编辑表单、AI 新词条 prompt、AI 补全字段均已接入。种子数据补全 IPA。
- **多词根/词缀模型**（#2）：新增 `roots[]` 数组，一个词可同时归属多个词根/词缀（如 reconstrucción → struct- / re- / con- / -ción）。`getRootKeys()` 聚合主词根+附加；词根列表按各词根分别计数分组；词根/词缀自身条目在词族中排首条（`getEntriesForRoot` 自条目优先）；详情卡词根显示为多枚可点击 chip。
- **跨语言同源/相关词补释义+发音**（#3）：cognates 扩展为 `{lang,word,ipa,meaning}`；同根词 Familia 若库内已有则显示释义+IPA 且可点击跳转；prompt 要求每个 cognate 带发音和中文释义。
- **形态拆解语素点击跳转**（#4）：breakdown 各语素可点击 → 高亮对应词根/词缀并切到词根详情（不筛选）。
- **AI 补全不阻塞**（#5）：`applyCompletions` 单字段 try/catch，某字段赋值失败（如只读属性）静默跳过，不阻断整批，不动无关标签。
- **阴阳性徽章配色 + 中文化**（#6/#10）：阳性=白底黑字实心、阴性=空心白字（`genderBadge`）；显示为中文「阳/阴」（`genderLabel`，数据仍存 m/f）。所有属性标签中文化。
- **PCIC 官方分类体系**（#7）：语义标签一级大类换为 Instituto Cervantes《Plan Curricular》Nociones Específicas 官方 20 类（中文标签）。`_routeTagToRoot` 重写路由到 PCIC；`migrateTaxonomyToPCIC()` 一次性迁移历史数据（旧→新映射 + 版本守卫）；种子数据、AI prompt 全部对齐。详见 ADR 0003。
- **单击/双击交互重构 + 三系统并行**（#8）：单击词源/词条=仅高亮+详情，不筛选、不进入分组；双击词源→跳到首个单词、双击词条→反向联动到主词根，均不筛选；仅「导图字母」「词根分组标题」触发筛选。搜索/标签/词根三系统并行求交（`getVisibleEntries`），互不清空。详见 ADR 0004。
- **全部词源/仅词根/仅词缀筛选**（#9）：左栏标题改「全部词源」，新增类型筛选按钮（`setRootTypeFilter` + `classifyRoot` 词缀分类）。此前按钮调用未定义函数（报错），本次补齐。
- **Bug 修复**：`saveEntry` 编辑时用展开 existing 保留表单未覆盖字段（此前会清空 gender/cognates/verbClass/regularity/register/frequency 等，造成编辑丢数据）。

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
