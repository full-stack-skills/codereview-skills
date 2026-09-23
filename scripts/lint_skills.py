#!/usr/bin/env python3
"""检查本仓技能的名称、frontmatter、引用和仓库边界。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
EXPECTED = {
    "codereview-context-impact",
    "codereview-finding-triage",
    "codereview-fix-verify",
    "codereview-rules",
    "codereview-scan",
}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def validate() -> None:
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if actual != EXPECTED:
        fail(f"技能集合不一致：缺失={sorted(EXPECTED - actual)}；未声明={sorted(actual - EXPECTED)}")
    for name in sorted(actual):
        if not NAME.fullmatch(name):
            fail(f"非法技能名：{name}")
        directory = SKILLS / name
        entry = directory / "SKILL.md"
        if not entry.is_file():
            fail(f"缺少 SKILL.md：{name}")
        content = entry.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            fail(f"缺少 YAML frontmatter：{name}")
        parts = content.split("---\n", 2)
        if len(parts) < 3:
            fail(f"frontmatter 未闭合：{name}")
        header = parts[1]
        if f"name: {name}\n" not in header:
            fail(f"name 与目录不一致：{name}")
        description = next((line.removeprefix("description: ") for line in header.splitlines() if line.startswith("description: ")), "")
        if not description or len(description) > 1024:
            fail(f"description 缺失或过长：{name}")
        if "何时" not in description and "时使用" not in description:
            fail(f"description 未说明触发场景：{name}")
        if len(content.splitlines()) >= 500:
            fail(f"SKILL.md 超过 500 行：{name}")
        if "license: Apache-2.0" not in header:
            fail(f"缺少 license：{name}")
        for markdown in directory.rglob("*.md"):
            source = markdown.read_text(encoding="utf-8")
            for target in LINK.findall(source):
                if target.startswith(("https://", "http://", "#")):
                    continue
                relative = target.split("#", 1)[0]
                resolved = (markdown.parent / relative).resolve()
                if directory.resolve() not in resolved.parents and resolved != directory.resolve():
                    fail(f"跨技能相对引用：{markdown}: {target}")
                if not resolved.exists():
                    fail(f"失效引用：{markdown}: {target}")
    print(f"Validated {len(actual)} CodeReview skills")


if __name__ == "__main__":
    validate()
