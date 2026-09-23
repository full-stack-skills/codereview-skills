# 核实记录样例

```text
候选：HEAD abc123 + index fingerprint 4c9…
执行：success；reviewed 3；skipped 1（二进制）；excluded 2（生成文件）
发现 A：src/PaymentService.java:82，confirmed/high
证据：重试分支在检查幂等记录之前调用 transfer；同一 request_id 重放两次可触发两次外部请求。
建议：将幂等状态检查移到外部调用前，并补重放测试。
发现 B：src/PaymentService.java:110，needs_verification/unknown
证据缺口：无法确认下游 transfer 接口自身是否幂等；不能据此宣称资金重复扣减已发生。
用户处置：未决定。
```

## 误报与覆盖判断

- 报告说空指针，但前置分支通过不可变类型保证非空：引用具体路径和约束，标误报；不能仅说“看起来安全”。
- 报告行号 `0` 或指向删除行：查看候选版本，找到可定位的新代码；若无法定位，保留问题但注明“位置未证实”。
- OCR 返回 0 条评论，但有 failed/budget 或 skipped 文件：报告“部分审查/未完成”，绝不写“通过”。
- 用户说“忽略这条”：记录处置，不把 confirmed 改成 false_positive。
