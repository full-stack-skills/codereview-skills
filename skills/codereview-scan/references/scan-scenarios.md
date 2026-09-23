# 扫描场景决策

| 用户意图 | 对象 | 建议入口 |
| --- | --- | --- |
| “检查我待提交的代码” | 暂存候选 | `codereview-plugin` harness；不要直接 scan |
| “审查这个 PR 相比 main 的变化” | 分支差异 | 官方 `open-code-review`；不做全库 scan |
| “接手这个模块，找已有的逻辑风险” | 指定完整目录 | `ocr scan --path <目录>` |
| “全仓做一次基线审计” | 完整仓库 | 用户确认范围、模型/预算后 `ocr scan` |

报告示例：

```text
范围：services/order，完整文件；非当前提交快照
执行：partial；OCR-managed；模型及端点已向用户披露
覆盖：42 个文件完成、3 个因预算跳过、5 个生成文件排除
重点：OrderService.java:184 的重复回调风险待下游契约核实
结论：已扫描部分发现上述风险；未扫描文件与未来提交不在结论范围
```

## 续跑注意

OCR 文档说明 range/commit review 与 scan 可续跑；普通 workspace review 的续跑支持不同。不要把 `review --resume` 与 `scan --resume` 混用。会话标识来自真实 OCR 输出或 `ocr session list`，不能猜。
