# codereview-skills

可独立安装的 CodeReview 工作流技能。OCR 的文件选择、规则匹配和模型执行属于 [Alibaba Open Code Review](https://github.com/alibaba/open-code-review)；本仓只补充需求上下文、跨文件影响、发现核实、修复验证、规则治理与全文件扫描等工作流。

```bash
npx skills add full-stack-skills/codereview-skills
npx skills add alibaba/open-code-review --skill open-code-review
npx skills add alibaba/open-code-review --skill open-code-review-delegate
```

| 技能 | 使用时机 | 产出 |
| --- | --- | --- |
| `codereview-context-impact` | 跨模块改动、需求约束需要进入审查 | 有出处的业务背景、影响路径和待核对假设 |
| `codereview-finding-triage` | OCR 发现需要核实或可能误报 | 逐条证据、状态与覆盖缺口 |
| `codereview-fix-verify` | 用户明确要求修复审查问题 | 最小修复、测试结果、新候选重审 |
| `codereview-rules` | 用户要制定项目专属 OCR 审查规则 | 可验证的规则变更与匹配样例 |
| `codereview-scan` | 无合适 diff，需审计目录或仓库 | 明确范围、覆盖限制的全文件扫描报告 |

提交前的选择、会话静默、候选快照和证据状态由 [`codereview-plugin`](https://github.com/full-stack-plugins/codereview-plugin) 的插件专属 `codereview-harness` 管理。手动运行上游 OCR 技能不会自动继承插件的提交授权；它们的工作区模式也不等同于“仅暂存内容”。报告始终是建议，不代替 CodeGuard 的可执行检查或 FlowGuard 的流程裁决。

独立安装只提供技能知识，不安装 OCR CLI，也不保证宿主插件已加载。实际安装、模型调用和跨宿主运行需要各自验证。

## 验证

```bash
python3 scripts/lint_skills.py
```

TRACE 基分与人工语义校准记录见 [TRACE_EVALUATION.md](TRACE_EVALUATION.md)；离线结构分不代表真实宿主触发率或审查发现率。

本仓采用 Apache-2.0。官方两个技能仍归 Alibaba 上游维护，未复制到本仓。
