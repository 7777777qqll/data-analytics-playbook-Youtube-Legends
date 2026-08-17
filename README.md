# Data Analysis YouTube Playbook

A Codex skill for practical, business-facing data analysis workflows inspired by high-performing data analysis educators and dashboard builders.

It helps Codex process spreadsheets, CSVs, Feishu/Lark sheets, Excel reports, campaign data, creator data, ROI analyses, sales data, and operational datasets into clear Chinese reporting outputs.

## What It Does

- Preserves raw data and creates separate cleaned or optimized outputs.
- Uses Chinese-facing field names, sheet names, KPI labels, chart titles, and conclusion headings by default.
- Structures analysis deliverables with summary-first reporting: KPI cards, segment tables, then traceable detail rows.
- Standardizes dates, IDs, numeric fields, percentages, ROI, blank values, and outlier checks.
- Encourages auditable metric definitions and row-count reconciliation before delivery.

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   └── validate_skill.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Installation

Copy this folder into your Codex skills directory:

```bash
cp -R data-analysis-youtube-playbook ~/.codex/skills/
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\data-analysis-youtube-playbook"
```

Restart or refresh Codex so the skill list can discover it.

## Usage

Example prompts:

```text
Use $data-analysis-youtube-playbook to analyze this Excel order detail file and output a Chinese report workbook.
```

```text
调用 data-analysis-youtube-playbook，帮我清洗这张投放明细表，输出中文字段、分类汇总和结论。
```

## Validation

Run the lightweight validator:

```bash
python scripts/validate_skill.py .
```

The validator checks:

- `SKILL.md` exists.
- YAML frontmatter contains `name` and `description`.
- Skill name follows lowercase hyphen-case.
- Required UI metadata file exists.

## Notes

This repository intentionally keeps the operational skill instructions in `SKILL.md`. GitHub-facing files such as this README and the license are included for publication, maintenance, and discoverability.
