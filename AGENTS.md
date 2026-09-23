# codereview-skills 维护边界

- 本仓只维护五个可独立安装的通用工作流技能。不要复制或改写 Alibaba 官方 `open-code-review`、`open-code-review-delegate` 技能；插件仓以固定上游版本引用它们。
- 不在本仓实现 OCR 引擎、宿主 Hook、提交授权、Git 暂存快照或最终门禁。插件专属 harness 在 `full-stack-plugins-repositories/codereview-plugin` 维护。
- 技能内容变更后运行 `python3 scripts/lint_skills.py`，并从工作区根目录运行 `./scripts/evaluate-package.sh codereview-skills`。不得以 TRACE 分数替代真实任务验收。
- 发布版本使用新 tag；不得移动已发布 tag。不要在技能中默认安装/升级 OCR、调用模型、发送代码、修改规则或自动提交。
- Markdown、注释与提交消息使用中文；技能 frontmatter `name` 与目录名一致，`SKILL.md` 小于 500 行，引用文件只链接本技能内部资源。
