# 开发日志 · DEVLOG

> 实现「为什么这么做 + 怎么实现 + 踩了什么坑」。技术细节、根因。
> 三姊妹项目（韩/日/西）共享架构，**通用要点见 `../Korean/DEVLOG.md`**（highlight/filter 解耦、LLM provider 缓存、AI 补全 emoji 修饰字段、移动端输入不放大、Gist 同步等）。本文件只记西语特有部分。

---

## 西语特色：词根本身是独立语言单位（词根详情面板）

### 与韩/日的根本差异
韩语的"词根"是初声下的分组（getX Roots），日语的"音根"是音根 key，二者都只是**导航分组**，没有独立实体。
西语的词根（hel-/gel-/am-/struct-）本身是**有意义的语言单位**：有释义、拉丁语源、音变、cognate、衍生词族。所以词根需要自己的"主页"。

### 实现（西2）
- `getRootMeta(root)`：聚合该词根下所有词条的元信息（取第一个有值的词条）。
- `renderRootDetail(panel, root)`：单击词根时，详情面板渲染词根聚合视图：
  - 词根释义（rootMeaning）
  - 拉丁语源（latinOrigin）
  - 词根语义分析（analysis，取代表词条）
  - 词源追溯（etymology）
  - 跨语言同源（englishCognate + cognates[]）
  - **同根词族列表**（每个词可双击进词条详情）
  - 语义标签聚合
- `selectRoot`：单击设 highlightRoot + **清空 selectedEntryId**（这样 renderDetail 切到词根详情分支）。
- `renderDetail`：`if (!selectedEntryId && highlightRoot) renderRootDetail(...)`。

### 双击 vs 单击
- 单击词根 → 词根详情面板（词族总览）
- 双击词条 → 该词条详情（形态拆解可视化）

---

## 索引模型：按单词实际首字母（不是按拉丁词根）

### 问题
helado 和 gelatina 共享拉丁源 gelatus，但 hel- 经历 g→h 音变。该归 H 还是 G？

### 决定
按**单词实际首字母**索引：helado→H，gelatina→G。hel-/gel- 的共同拉丁源作为「跨语言同源」展示，不混索引。符合"看到一个新词先看首字母"的认知习惯。

### 后缀/前缀
`-ado` 按首字母 A 索引，type='后缀'，详情卡显示后缀 badge。

---

## 形态拆解可视化（西语核心教学价值）

### 设计
西语单词 = 前缀 + 词根 + 连接元音 + 后缀 + 屈折词尾。详情卡把 breakdown 字符串拆成彩色语素。

### 实现 `renderMorphology(breakdown)`
- breakdown 格式：「re-(再) + con-(共同) + struct-(建造) + -ción(动作名词后缀)」
- 按 `+` 分割，每段正则提取 `词素(释义)`。
- 分类：`-开头` → 后缀（绿）；在 `PREFIXES` 集合（re-/con-/de-/pre-…）→ 前缀（琥珀）；否则 → 词根（蓝）。
- 坑：词根也可能以 `-` 结尾（如 struct-、hel-），不能纯靠尾 dash 判定前后缀。用 PREFIXES 白名单 + 首 dash 判后缀。

---

## A-Z 字母导图（对应韩语五音、日语语义层）

### 数据
`LETTERS`：27 字母，每字母含三层（源自设计文档）：
- `proto`：腓尼基/拉丁史源（如 A=aleph 牛头）
- `action`：发音动作与音感（如 B=双唇闭合爆破）
- `image`：可建立的核心意象（如 B=房屋/身体/鼓包）

### 分组
`LETTER_GROUPS_ORDER`：按发音部位 8 组（元音/双唇音/齿音/软腭音/腭音/擦音/流音/罕见借词），每组一种颜色。对应韩语的五音分组。

---

## 拉丁→西语音变矩阵（对应韩语造物主矩阵）

`SOUND_CHANGES`：核心音变规则（f→h、ĕ→ie、ŏ→ue、pl/cl/fl→ll、-ct→ch、双拉丁词）。AI prompt 引用此表生成词源分析。这是西语词源教学的核心——同一拉丁源常产生通俗继承词（音变）+ 文艺复兴书面借词（保留拉丁形）一对词，如 fragua/fábrica。

---

## 20 大类语义标签（西语学习语境定制）

不同于韩语照搬分類語彙表，西语用学习语境的大类：饮食·食物·烹饪 / 身体·健康·医疗 / 情感·心理·性格 / 自然·天文·地理·生物 / 动作·行为·过程 / 状态·性质·变化 等 20 个。`_TAG_SUB_EXAMPLES` 每类配二级子类示例。`_TAG_ROOT_ROUTER` 按中/西关键词路由。

---

## 本次会话补齐的通用特性（详见韩语 DEVLOG）

- LLM 双配置 + provider 缓存（`onProviderChange` oldProvider 捕获）
- AI 新词条（深度词源分析 prompt）+ AI 补全（字段配置）+ AI 释义 emoji（修饰字段）
- 多端同步 Gist + PWA + CORS 代理
- 移动端输入不放大、清搜清签、双击联动、最近添加抽屉
