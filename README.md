# Competitive Analysis Skill

A reusable Codex skill for product and feature competitive analysis.

This skill helps Codex follow a stronger product-research workflow:

- clarify the real goal before researching
- ask only the minimum necessary scoping questions
- research official definitions first
- add screenshots, user comments, and supporting evidence when useful
- produce both a research draft and a presentation-friendly version

## What this skill is for

Use this skill when you want Codex to do:

- competitive analysis
- competitor research
- feature benchmarking
- metric naming / definition research
- product page / UX comparison
- user-comment synthesis
- industry or scientific evidence gathering

This skill is optimized for `product / feature-level` analysis.

It does **not** default to broader market strategy work like pricing, channels, or GTM analysis unless the user explicitly asks for that.

## Install

### Recommended: install from GitHub

```bash
git clone https://github.com/cookiexjw/competitive-analysis.git
cd competitive-analysis
bash install.sh
```

What this does:

- creates `~/.codex/skills/competitive-analysis/`
- copies the skill files into that folder
- makes the skill available to Codex on this machine

### Manual install

If you prefer not to run the install script:

```bash
mkdir -p ~/.codex/skills/competitive-analysis
cp -R competitive-analysis/. ~/.codex/skills/competitive-analysis/
```

After installation, the structure should look like:

```bash
~/.codex/skills/competitive-analysis/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── questionnaire.md
│   ├── research-workflow.md
│   ├── output-templates.md
│   └── source-policy.md
└── scripts/
    └── generate_report_html.py
```

## How to use it

After installation, ask Codex things like:

- `做竞品分析`
- `帮我做一版竞品调研`
- `对标一下这个功能`
- `查一下类似的指标 / 页面 / 体验`
- `benchmark this feature`
- `do a competitive analysis`

By default, the skill will guide Codex to:

1. clarify the goal
2. ask the minimum necessary scoping questions
3. define the competitor pool
4. research official sources first
5. add user-comment patterns and media reviews when useful
6. add scientific / industry evidence when needed
7. output a research draft, a readable report version, and optionally an HTML preview

## Share this with others

You can share this repository directly.

If someone wants to install it, send them this:

```bash
git clone https://github.com/cookiexjw/competitive-analysis.git
cd competitive-analysis
bash install.sh
```

After that, they can use it in Codex by saying:

```text
做竞品分析
```

or:

```text
帮我做一版竞品调研
```

If they ask more broadly, the skill is also meant to trigger on requests like:

- `对标分析一下这个功能`
- `查一下类似产品怎么做`
- `帮我看一下主流竞品的页面和用户评价`

## What the skill contains

- `SKILL.md`: trigger conditions, workflow rules, and output expectations
- `references/questionnaire.md`: the minimum scoping questions to ask first
- `references/research-workflow.md`: default research process
- `references/output-templates.md`: report structure templates
- `references/source-policy.md`: source priority and evidence rules
- `scripts/generate_report_html.py`: a template script for generating a readable HTML report from Markdown

## Notes

- This repository contains the skill itself, not project-specific competitive analysis outputs.
- The content is intentionally generic and shareable.
- Official sources are prioritized. User comments and community posts are used as supporting qualitative input, not as official definitions.

## License

MIT
