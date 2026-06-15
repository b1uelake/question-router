# Question Router（问题路由器）

一套框架无关的提示方法论，将模糊、不完整的问题转化为结构清晰的高质量回答。它对请求进行分类、检查上下文充分性、只问必要的澄清问题、加载对应的回答契约，并在最终输出前进行质量校验。

这套指令可以作为**系统提示词**用于任何基于 LLM 的 agent —— Claude Code、Codex、Cursor、Windsurf、ChatGPT、LangChain 或你自己搭建的 agent。本仓库使用了 Codex 的 skill 格式（YAML frontmatter + markdown），但方法论本身与平台无关。

## 工作原理

每个问题经过一个结构化的流水线：

1. **分类** — 确定问题的主要类型
2. **检查上下文** — 识别缺失但会实质性影响回答的信息
3. **澄清（按需）** — 问最少的有用问题（1–3 个，最多 5 个）
4. **加载契约** — 应用对应类型的回答结构
5. **质量校验** — 在输出前通过质量门

### 六种问题类型

| 类型 | 适用场景 | 示例 |
|------|---------|------|
| `learning`（学习） | 概念、解释、学习路径 | "pytest 是什么？" |
| `analysis`（分析） | 因果、权衡、对比、"为什么"类问题 | "为什么创业公司选微服务而不是单体？" |
| `decision`（决策） | 选择、优先级、是否采用 | "我该用 React 还是 Vue？" |
| `plan`（计划） | 路线图、学习计划、分步方案 | "给我做一个 10 周的 AI 学习计划" |
| `risk`（风险） | 失败模式、安全、合规、隐患 | "跳过 GDPR 合规安全吗？" |
| `technical`（技术） | 实现、调试、架构、部署 | "我的 API 高负载时返回 502" |

## 回答结构

每个完整回答包含九个必要要素：

1. **问题类型** — 分类和问题框架
2. **假设** — 从不完整上下文中推断出的内容
3. **已知事实** — 有来源支撑或广泛公认的信息
4. **合理推断** — 从已知事实推导出的结论
5. **建议** — 带置信度的可操作指导
6. **不确定性 / 需验证项** — 哪些需要进一步确认
7. **判断标准** — 用于评估选项的准则
8. **反例或失败场景** — 回答在什么情况下不成立
9. **优先级行动步骤** — 有序、具体的下一步

对于简单的入门问题，紧凑模式将其压缩为：类型、直接回答、为什么重要、示例、下一步。

## 仓库结构

```
question-router/
├── SKILL.md                           # Skill 定义和核心工作流
├── references/                        # 各类型的回答契约
│   ├── learning.md
│   ├── analysis.md
│   ├── decision.md
│   ├── plan.md
│   ├── risk.md
│   └── technical.md
├── evals/
│   └── evals.json                     # 回归测试用例
├── schemas/
│   ├── eval-case.schema.json          # 评估用例的 JSON Schema
│   └── route.schema.json              # 内部路由对象的 JSON Schema
└── scripts/
    ├── validate_skill.py              # 校验 skill 结构和评估数据
    ├── build_promptfoo_config.py      # 生成 promptfoo 评估配置
    └── run_evals.sh                   # 完整评估流水线（校验 → 构建 → 运行）
```

## 使用方式

这套方法论适用于任何 LLM agent。根据你的场景选择：

### 作为 Codex / Claude Code skill

```bash
git clone https://github.com/b1uelake/question-router.git ~/.codex/skills/question-router
```

当你提出宽泛、模糊或复杂的问题时，skill 会自动激活。

### 作为系统提示词（任意 agent）

将 `SKILL.md` 和相关 `references/*.md` 复制到你的系统提示词或自定义指令中。文件都是纯 markdown，不需要特殊格式。

### 作为 LangChain / 自定义 agent 提示词

将 `SKILL.md` 和各回答契约加载到 agent 的指令模板中。`evals/evals.json` 中的评估套件提供了回归测试用例，可用于你自己的评估流水线。

### 运行校验

```bash
cd ~/.codex/skills/question-router
python3 scripts/validate_skill.py
```

### 运行评估套件

```bash
# 需要 promptfoo：npm install -g promptfoo
bash scripts/run_evals.sh
```

评估脚本默认使用 Codex 风格的 HTTP API 端点。要使用其他提供商（OpenAI、Anthropic 等），传入自定义配置或编辑 `scripts/build_promptfoo_config.py`。

## Codex 特定格式说明

本仓库使用 Codex 的 skill 格式（`SKILL.md` 带 YAML frontmatter）。这只是薄封装 —— 核心方法论在于回答契约和 `SKILL.md` 中的分类逻辑，它们都是纯 markdown。你可以去掉 YAML frontmatter，剩余部分即可在任何 agent 框架中使用。

## 设计原则

- **能问就不要猜。** 缺失的上下文如果会实质性改变回答，触发澄清（1–3 个问题，最多 5 个）。
- **能假设就不要问。** 如果安全默认值能处理歧义，直接声明假设并继续。
- **结构随复杂度缩放。** 简单入门问题用紧凑模式，高风险决策用完整的九要素结构。
- **事实、推断、建议三者分离。** 读者应始终清楚哪个是哪个。
- **每条建议都需要标准。** "选 X"但没有"因为在条件 Z 下 Y"是不完整的。
- **标记验证需求。** 法律、合规、定价和依赖来源的论断必须标注需要验证。

English version: [README.md](README.md)

## 许可证

MIT
