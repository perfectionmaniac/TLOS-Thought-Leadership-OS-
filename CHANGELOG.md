# Changelog

All notable changes to TLOS are recorded here, reconstructed from the actual
git commit history (all commits landed on 2026-07-27 and 2026-07-28 — this
project was built in one continuous burst, not over a longer calendar
period).

## v0.1.0 — Product Foundation (2026-07-27)
Initial scaffold: README, `docs/` (manifesto, principles, architecture,
decision log, roadmap, repository structure, glossary), `founder/FOUNDER_GUIDE.md`,
`project/PRODUCT_BACKLOG.md`, `releases/RELEASE_NOTES_v0.1.0.md`, and empty
placeholder folders (`analytics/`, `automation/`, `knowledge/`, `research/`,
`skills/`, `templates/`). This describes an early, more generic vision of TLOS
(voice-memo ingestion, Whisper transcription, multi-channel publishing) that
predates the LinkedIn-focused system actually built afterward — it was never
updated to reflect what shipped from v0.2.0 onward.

## v0.2.0 — Product Backlog & Chief Content Strategist (2026-07-27)
Product backlog (epics, sprints, definition of done) and the first specialist
skill, Chief Content Strategist.

## v0.3.0 — Positioning Expert (2026-07-27)
## v0.4.0 — Research Analyst (2026-07-27)
## v0.5.0 — LinkedIn Writer (2026-07-27)
## v0.6.0 — Content Orchestrator, Kernel (2026-07-27)
Early 42-line orchestrator kernel — superseded by the full Content
Orchestrator workflow in v0.15.0.

## v0.7.0 — TLOS Manifest (2026-07-27)
`tlos.yaml`, the machine-readable system manifest.

## v0.8.0 — End-to-End Content Production Workflow Engine (2026-07-27)
## v0.9.0 — Founder Voice Engine (2026-07-27)
## v0.10.0 — LinkedIn Growth Operating System (2026-07-27)
Early version — superseded by the expanded LinkedIn Growth OS workflow in
v0.14.0.

## v0.11.0 — LinkedIn Analytics Intelligence Engine (2026-07-27)

## CR-012 — Personal LinkedIn Intelligence Report v1.0 (2026-07-27)
Completed with real founder LinkedIn data (audience + content analytics,
27 Jul 2025 – 26 Jul 2026): 5,115 impressions, 2,212 members reached, 5,494
followers, and a repositioning thesis toward HR tech / frontline workforce /
fintech.

## CR-013 — LinkedIn Data Analysis Engine (2026-07-27)
Capability specification, LinkedIn Intelligence Input Layer, and output
contracts.

## Repository maintenance (2026-07-27)
`.gitignore` added, `.DS_Store` cleanup, and README documentation added for
`engines/`, `inputs/`, `reports/`, and `workflows/`.

## v0.14.0 — LinkedIn Growth OS (2026-07-27)
Expanded LinkedIn Growth OS workflow (still status: Draft — not yet formally
approved).

## v0.15.0 — Content Orchestrator, Advanced Operating Layer (2026-07-27 – 2026-07-28)
The current canonical orchestrator (`workflows/content_orchestrator.md`,
"Approved for Release 1.0") — unifies the LinkedIn-intelligence side
(LinkedIn Growth OS, Personal LinkedIn Intelligence Report, LinkedIn Data
Analysis Engine, Research Engine) with the generic content-lifecycle side
(Writing Engine, Review Engine, Publishing Workflow, Performance Analytics,
Knowledge Repository) into one pipeline.

## v0.16.0 — Writing Engine (2026-07-28)
## Release 17 — Review Engine (2026-07-28)
## Release 18 — Publishing Workflow (2026-07-28)
## Release 19 — Performance Analytics (2026-07-28)

## Knowledge Repository (2026-07-28)
`knowledge/Knowledge Repository.md` — the memory/organisational-learning
capability referenced throughout the pipeline as "Release 20" in earlier
planning chats.

## Learning Intelligence Engine & Recommendation Engine (2026-07-28)
`engines/learning-intelligence-engine/` (Approved) and
`engines/recommendation-engine/` (Draft).

## Universal AI Operating Layer, SKILL-001 – SKILL-009 (2026-07-28)
AI Operating Principles, Expert Council Engine, Thinking Framework,
Knowledge Management, Memory & Context, Recommendation Framework, Workflow
Execution, Quality Assurance, Output Formatting. A platform-agnostic
reasoning kernel, not yet wired into the LinkedIn/content pipeline above.

---

## Unreleased / in progress

- **Repository integrity fixes**: `tlos.yaml` and nine `skills/`/`workflows/`
  files were discovered to be raw `.docx` binaries mistakenly saved with a
  `.md` extension (readable in a text editor as garbage, and invisible on
  GitHub's file viewer). All ten were recovered and rewritten as clean
  Markdown/YAML with their original content preserved verbatim.
- **`automation/` engine**: the first real, executable implementation of the
  Content Orchestrator pipeline (Python, calling Claude + optionally
  Perplexity), built directly against the approved spec files above.
- **CR-016 — Founder Brand Intelligence Layer**: not yet started.
