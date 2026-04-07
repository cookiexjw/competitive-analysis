# Competitive Analysis Skill

A reusable Codex skill for product and feature competitive analysis.

This skill is designed to help Codex produce outputs similar to a strong product research workflow:

- clarify the goal before researching
- ask the minimum necessary scoping questions
- research official definitions, user comments, screenshots, and supporting evidence
- produce both a research draft and a presentation-friendly readable version

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

## What it does by default

When triggered, the skill guides Codex to:

1. understand the real goal
2. ask the minimum necessary questions
3. define the competitor pool
4. research official sources first
5. add user-comment patterns and media reviews when useful
6. add scientific / industry evidence when needed
7. output:
   - a research draft
   - a more readable report version
   - optionally an HTML preview-friendly version

## Installation

Copy the `competitive-analysis` folder into your Codex skills directory:

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

## Typical trigger phrases

This skill should trigger when the user says things like:

- “做竞品分析”
- “帮我做一版竞品调研”
- “对标一下这个功能”
- “查一下类似的指标 / 页面 / 体验”
- “benchmark this feature”
- “do a competitive analysis”

## Output style

The skill is designed to produce two layers of output:

### 1. Research draft

For information completeness and internal knowledge capture:

- key findings first
- competitor landscape
- detailed competitor breakdown
- insights and opportunity areas
- candidate frameworks / metric dimensions
- sources

### 2. Readable presentation version

For review and discussion:

- shorter conclusions
- stronger section titles
- screenshot-integrated competitor sections
- “why it matters / screenshots / observations / implications / risks”

## Included files

- `SKILL.md`: trigger conditions, workflow rules, and output expectations
- `references/questionnaire.md`: the minimum scoping questions to ask first
- `references/research-workflow.md`: default research process
- `references/output-templates.md`: report structure templates
- `references/source-policy.md`: source priority and evidence rules
- `scripts/generate_report_html.py`: template script for generating a readable HTML report from Markdown

## Notes

- This repository contains the skill itself, not project-specific competitive analysis outputs.
- The content is intentionally generic and shareable.
- Official sources are prioritized. User comments and community posts are used as supporting qualitative input, not as official definitions.

## License

MIT
