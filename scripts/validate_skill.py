#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md frontmatter must be closed with ---")
    block = text[4:end].strip()
    data = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    skill_md = root / "SKILL.md"
    openai_yaml = root / "agents" / "openai.yaml"

    if not skill_md.exists():
        fail("Missing SKILL.md")
    if not openai_yaml.exists():
        fail("Missing agents/openai.yaml")

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name:
        fail("Frontmatter missing name")
    if not description:
        fail("Frontmatter missing description")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"Invalid skill name: {name}")
    if len(description) < 80:
        fail("Description should be specific enough to trigger correctly")
    if "TODO" in text:
        fail("SKILL.md contains TODO")

    print(f"OK: {name}")


if __name__ == "__main__":
    main()
