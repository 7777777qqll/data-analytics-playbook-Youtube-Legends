---
name: data-analysis-youtube-playbook
description: Data analysis workflow inspired by high-performing YouTube data analysis educators such as Alex The Analyst, Luke Barousse, freeCodeCamp, StatQuest, Chandoo, and Guy in a Cube. Use when Codex needs to clean, analyze, summarize, visualize, optimize, or restructure spreadsheets, CSVs, Feishu/Lark sheets, Excel reports, dashboards, ROI analyses, campaign data, creator data, sales data, or operational datasets into Chinese business conclusions and reusable reporting outputs.
---

# Data Analysis YouTube Playbook

## Core Workflow

1. Clarify the business question before touching the data.
   - Identify the decision, comparison baseline, target metric, segmentation, and time window.
   - If the user gave a clear goal, proceed without asking.

2. Preserve source data.
   - Do not overwrite raw sheets or raw files.
   - Create a new sheet/file for cleaned data, analysis, or optimized reporting.
   - Keep original row identifiers when available.

3. Build a field map.
   - Identify dimensions: date, category, project, user/creator, channel, city, product, campaign.
   - Identify measures: spend, GMV, revenue, orders, views, clicks, conversions, ROI, rate, count.
   - Identify derived fields needed for analysis: month, week, category group, status, link type, tier, bucket.

4. Clean and standardize.
   - Normalize dates.
   - Standardize category names and blank values.
   - Preserve IDs, handles, URLs, phone-like values, and codes as text.
   - Treat money, counts, percentages, and ROI as numeric values.
   - Flag missing values, duplicates, impossible values, and outliers.

5. Explore before concluding.
   - Calculate overall KPIs.
   - Compare by category, month, project, level, city, creator, channel, and investment bucket when relevant.
   - Look for concentration, long-tail effects, abnormal rows, and sample-size problems.
   - Always show numerator, denominator, and sample size for rates.

6. Use clear metric definitions.
   - ROI = return / investment unless the user or source document defines another formula.
   - Lift % = (new metric - baseline metric) / baseline metric.
   - Share % = segment value / total value.
   - For weighted averages, use total numerator / total denominator, not the mean of row-level rates.

7. Structure output like an analyst report.
   - Top section: title, source, time range, KPI cards, key conclusion.
   - Middle section: summary tables by category/time/top contributors.
   - Bottom section: detailed table with filters.
   - Add notes for assumptions, exclusions, and data quality issues.

8. Make conclusions selective.
   - Lead with high-impact findings.
   - Avoid generic overall conclusions when the user asks for category-level or segment-level results.
   - Suppress low-impact or noisy findings unless they explain a risk.

9. Validate before delivery.
   - Reconcile row counts against the source.
   - Spot-check first, middle, and last records.
   - Verify KPI totals match detail rows.
   - For online sheets, write back and then read back.
   - State data limitations clearly.

## Chinese Output Rules

Use Chinese as the default output language for data-facing deliverables unless the user explicitly requests otherwise.

- Use Chinese for main column headers, sheet names, chart titles, KPI labels, notes, and conclusion headings.
- Prefer business-readable Chinese field names: `项目时间`, `分类`, `项目`, `达人名`, `城市`, `投资规模`, `实际ROI`, `最佳段ROI`, `提升幅度`, `核销GMV`, `投放金额`, `记录数`, `占比`.
- Keep original identifiers unchanged when literal preservation matters: IDs, account handles, URLs, order numbers, SKU codes, formulas, and system field names.
- If the source fields are English, output a Chinese-facing version and keep original field names only when traceability requires it, such as `原字段名`.
- For bilingual deliverables, put Chinese first and English in parentheses only when helpful.

## Report Layout Rules

Use the reporting pattern learned from strong YouTube data-analysis tutorials and budget dashboard examples:

- Put results before raw detail.
- Use dark header bands for report titles and section headers.
- Use blue for source/input fields.
- Use green for calculated/output areas.
- Use yellow only for assumptions or manual inputs.
- Freeze headers and enable filters for long tables.
- Use readable column widths and wrap long project/link text.
- Keep raw detail traceable with source row number or source ID.

## Default Deliverables

For spreadsheet tasks, produce:

- A cleaned or optimized sheet/workbook.
- A summary block with KPI cards.
- Segment tables for requested dimensions.
- A detailed table preserving source traceability.
- A concise Chinese conclusion focused on decision usefulness.

## Decision Style

Be practical and business-facing:

- Say what changed.
- Say which segments matter.
- Say how large the effect is.
- Say what action should be prioritized.
- Say what data is missing if the conclusion is weak.
