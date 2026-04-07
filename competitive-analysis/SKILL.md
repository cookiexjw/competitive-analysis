---
name: competitive-analysis
description: Create product and feature competitive analysis reports. Trigger when the user asks for 竞品分析, 竞品调研, 对标分析, similar products/features research, or wants structured analysis of features, metrics, pages, user comments, screenshots, or supporting industry/scientific evidence. Always begin by clarifying the goal and asking the minimum necessary scoping questions before doing research.
---

# 竞品分析

这个 skill 用于 `产品/功能层面的竞品分析`，默认产出两类结果：

1. 研究底稿：信息完整，适合沉淀和继续加工
2. 导出版：更易读，适合评审、汇报和直接查看截图

## 何时使用

当用户出现以下意图时触发：

- 说“做竞品分析”“做竞品调研”“做对标分析”
- 想查“类似功能/指标/页面/体验/命名”的产品
- 想比较品牌、功能定义、指标含义、展示方式、用户评论
- 想为产品定义、PRD、设计方案、命名方案寻找对标

默认适用范围：

- 产品/功能竞品分析
- 指标、页面、体验、用户评论、科学依据等研究任务

默认不扩展：

- 定价、渠道、品牌营销、市场份额、商业战略
- 除非用户明确要求

## 必须遵守的工作方式

### 1. 先规划，再开始研究

如果用户只说“做竞品分析”，不要直接写报告。必须先做：

1. 看用户已有上下文和本地文件
2. 判断用户的真实目标
3. 提最少但关键的问题
4. 确认范围后再开始联网检索和输出

优先使用 `request_user_input` 来问问题；如果不可用，再用简洁的文本提问。

### 2. 默认要问的关键问题

先读 `references/questionnaire.md`。

最少应明确：

- 分析对象：功能 / 指标 / 页面 / 体验 / 健康依据
- 行业范围：全球主流 / 中国优先 / 垂直场景
- 输出用途：定义产品 / 做汇报 / 医学背书 / 设计参考
- 输出深度：快速盘点 / 标准研究 / 高密度图文稿

如果用户已经给足这些信息，只补问缺失项，不要机械重复。

### 3. 联网研究必须遵守来源优先级

先读 `references/source-policy.md`。

默认来源优先级：

1. 官方官网 / 官方帮助中心 / 官方产品页
2. 主流媒体评测
3. Reddit / 官方社区 / 论坛等用户评论
4. WHO / CDC / HHS / ACSM / AHA / PubMed 等权威来源

不要把论坛讨论当成官方定义，也不要把用户评论写成定量结论。

### 4. 研究流程

先读 `references/research-workflow.md`。

工作顺序必须尽量接近：

1. 明确目标和评判标准
2. 划定竞品池
3. 建立统一分析字段
4. 查官方定义
5. 查用户评论与媒体评价
6. 查必要的科学/行业依据
7. 提炼洞察、机会点、风险
8. 输出研究底稿
9. 需要时输出导出版和 HTML 查看版

### 5. 输出形态

先读 `references/output-templates.md`。

默认输出：

- 研究底稿
- 导出版

如果用户明确说“更易读”“像汇报稿”“打开直接看图”，则追加：

- 导出版 Markdown
- HTML 查看版

不要只给链接清单。要把截图、观点和结论整合进正文。

### 6. 截图与图片规则

- 优先官方图
- 官方图不足时，少量补论坛或真实使用截图
- 图片直接放在对应竞品分析小节，不要全部堆在附录
- 图片后要解释这张图说明了什么
- 如果图片无意义、空白、过于不稳定，明确标注“暂无图片”

### 7. 导出版修改要求

如果生成导出版或 HTML 查看版，要确保：

- 阅读顺序比研究底稿更清晰
- 截图放在对应段落，不单独堆链接
- 图片尺寸统一
- 图片可点击放大查看
- 小图或同类图可并排布局节省空间
- 空图位替换或标注“暂无图片”

## 输出建议

### 研究底稿

默认包含：

- 研究结论先看
- 竞品全景概览
- 重点竞品拆解
- 共性洞察
- 产品机会点
- 候选指标/能力框架
- 科学依据或行业依据
- 参考来源

### 导出版

默认包含：

- 更短的结论块
- 更强的小节标题
- 图文并行的竞品展示
- 页面示意 + 设计观察 + 对我们的启发

## 参考文件

- `references/questionnaire.md`：开始前提问模板
- `references/research-workflow.md`：研究流程
- `references/output-templates.md`：研究底稿和导出版模板
- `references/source-policy.md`：来源优先级和表达边界
- `scripts/generate_report_html.py`：Markdown 转 HTML 导出版模板
