# TLOS — Handoff to Claude Code

Paste this whole file as your first message in Claude Code (after you've extracted
`TLOS_update_v2.zip` into your actual local repo folder and opened that folder
in Claude Code). It gives Claude Code everything it needs to continue without
re-deriving any of this from scratch.

---

## What TLOS is

**TLOS (Thought Leadership Operating System)** is an AI-native pipeline that
takes a founder's raw ideas and real LinkedIn performance data and turns them
into researched, positioned, written, reviewed, and publish-ready LinkedIn
content — while learning from what performs well over time. Owner: Alok
Ranjan. It was designed across many ChatGPT sessions as a set of Markdown/YAML
specifications (in `skills/`, `workflows/`, `engines/`), and is now being
turned into a real, running system.

**Goal for "live":** a real working automation, not a chat prompt — actual
code that runs the pipeline, callable both on-demand and on a weekly
schedule. Priorities: keep hosting/infra costs minimal (lean, one-person
operation), reuse the repo's existing GitHub-based workflow (GitHub Desktop),
and don't over-engineer before the core pipeline is proven end to end.

## Current real state of the repo (verified directly, not guessed)

The repo had **41 real commits**, all landing in a two-day burst
(2026-07-27/28). Three different naming schemes used across different
ChatGPT sessions (`CR-XXX`, `vX.X.0`, `"Release N"`) turned out to be **the
same single sequence**, just labeled inconsistently — e.g. `v0.14.0 = CR-014`
(LinkedIn Growth OS), `v0.15.0 = CR-015 = "Release 15"` (the current 781-line
Content Orchestrator). Full reconstructed history is in `CHANGELOG.md`.

**What's built and Approved:** Content Orchestrator (`workflows/content_orchestrator.md`,
the canonical 781-line version — supersedes the old 42-line
`skills/Content_Orchestrator.md` kernel), Writing Engine, Review Engine,
Publishing Workflow, Performance Analytics, Knowledge Repository, Founder
Voice Engine, LinkedIn Analytics Intelligence Engine, LinkedIn Data Analysis
Engine, Chief Content Strategist, Positioning Expert, Research Analyst,
LinkedIn Writer. Plus a separate, not-yet-wired-in "Universal AI Operating
Layer" (`skills/001` through `009`: Operating Principles, Expert Council
Engine, Thinking Framework, Knowledge Management, Memory & Context,
Recommendation Framework, Workflow Execution, Quality Assurance, Output
Formatting).

**CR-012 (Personal LinkedIn Intelligence Report) is actually done**, with
real data: 5,115 impressions, 2,212 members reached, 5,494 followers
(27 Jul 2025 – 26 Jul 2026), and a thesis to reposition content toward HR
tech / frontline workforce / fintech instead of generic banking/finance.

**Not yet started:** CR-016 — Founder Brand Intelligence Layer. Also,
`workflows/linkedin_growth_os.md` (CR-014) is still status: Draft, not
formally Approved.

**Ten files were corrupted and have been fixed** (already applied in the zip
you extracted): `tlos.yaml` had lost all line breaks (rewritten as valid
YAML); nine files — `project/PRODUCT_BACKLOG.md`,
`skills/Content_Orchestrator.md`, `skills/Founder_Voice_Engine.md`,
`skills/Positioning_Expert.md`, `skills/Chief_Content_Strategist.md`,
`skills/Research_Analyst.md`, `skills/LinkedIn_Analytics_Intelligence_Engine.md`,
`skills/LinkedIn_Growth_OS.md`, `skills/LinkedIn_Writer.md`,
`workflows/content-production-workflow.md` — were secretly raw `.docx`
binaries saved with a `.md` extension (invisible in GitHub's file viewer,
unreadable as Markdown). All recovered and rewritten with original content
preserved verbatim. `CHANGELOG.md` was empty; it's now populated from real
git history.

One more layer worth knowing about: `docs/`, `README.md`, `founder/`, and
`releases/RELEASE_NOTES_v0.1.0.md` are the very first commit to the repo — an
early, more generic vision of TLOS (voice-memo/Whisper ingestion,
Substack/Medium publishing) that predates and doesn't match what was actually
built afterward. It was never updated. Treat `workflows/`, `skills/`,
`engines/` as the source of truth over `docs/`/`README.md` where they
disagree.

## What's already built in code (`automation/` folder)

A working Python engine, not yet run against real API keys:

- `automation/main.py` — CLI: `python main.py new "<idea>"` runs the full
  pipeline; `python main.py analyze-linkedin --audience X.xlsx --content Y.xlsx`
  runs the LinkedIn Data Analysis Engine.
- `automation/tlos_engine/specs.py` — loads the actual spec `.md` files from
  `skills/`/`workflows/`/`engines/` as LLM system prompts. This is the bridge
  between the specs and the code — edit a spec, the next run picks it up.
- `automation/tlos_engine/pipeline.py` — the orchestrator: Research →
  Positioning → Strategy → Founder Voice → Writing → Review (1 revision
  round) → Publishing package. Deliberately a simplified straight-through
  version of the fuller `content_orchestrator.md` decision framework — richer
  routing (6-question strategic gate, rejected drafts going back to strategy)
  is the natural next iteration once this simpler path is proven.
- `automation/tlos_engine/llm_clients.py` — Claude (Anthropic SDK) for
  orchestration/writing/review; Perplexity for grounded research.
  **Important**: Perplexity is deprecating the Sonar API in favor of a new
  Agent API, with Sonar support ending September 2026 (i.e., very soon
  relative to when this was written). Check https://docs.perplexity.ai for
  the current recommended endpoint before relying on this in production.
- `automation/tlos_engine/linkedin_ingest.py` — parses LinkedIn's exported
  `.xlsx` analytics files. Written before seeing a real export file, so it's
  deliberately generic — recalibrate column/sheet handling once you have a
  real file.
- `automation/README.md` — setup instructions (API keys, `.env`, running it).

**None of this has been run against real API keys yet** — verified to
compile and that every spec file it references loads correctly, nothing
more.

## Target architecture for "live"

- **Interface**: Telegram bot (free, phone-native, doubles as on-demand chat
  + push notifications for scheduled digests). Not built yet.
- **Usage pattern**: both a weekly scheduled run (pulls latest LinkedIn data
  if provided, prepares draft content for review) AND on-demand chat
  ("write me a post about X" → runs the pipeline, returns a draft). Both
  requested explicitly by the founder.
- **Hosting**: a small always-on host that deploys from GitHub — Railway or
  Render recommended (~$5-7/month), not a raw VPS (avoids server admin
  overhead for a non-technical, lean-cost operator). Not set up yet. Note: a
  Railway MCP connector is available if useful for deploying from inside a
  Claude session.
- **LinkedIn data**: no reliable API for personal profile analytics: exports
  stay a manual `.xlsx` download-and-feed-in step, not a live API pull.
- **Publishing**: intentionally NOT automatic posting to LinkedIn (no
  reliable API for that either) — the pipeline produces a ready-to-paste
  publishing package, copy/paste to LinkedIn is the final human step by
  design.

## What's next, in order

1. Get an Anthropic API key (console.anthropic.com → API Keys) and a
   Perplexity API key (perplexity.ai/settings/api) — Perplexity is optional,
   the pipeline works without it with less grounded research.
2. Set up `automation/.env` from `.env.example`, install
   `automation/requirements.txt`.
3. Run `python main.py new "<a real idea>"` and see what actually comes out —
   this is the first real end-to-end test. Fix whatever breaks (prompt
   issues, JSON-parsing edge cases, etc. — this has never been run live).
4. Get real LinkedIn `.xlsx` exports and test `analyze-linkedin`; recalibrate
   `linkedin_ingest.py` against the real file structure.
5. Build the Telegram bot interface (create via @BotFather, wire into
   `tlos_engine`).
6. Build the weekly scheduled digest job.
7. Deploy to Railway or Render; wire environment variables/secrets there.
8. Full end-to-end verification: one real idea through the full pipeline,
   one real weekly digest cycle.
9. Longer-term: decide whether/how to formally wire in the Universal AI
   Operating Layer (SKILL-001–009) as a governing reasoning layer; specify
   and build CR-016 (Founder Brand Intelligence Layer); reconcile or archive
   the stale `docs/`/`README.md` layer so it matches reality.

## Working style notes

Alok is non-technical but capable of following clear steps (uses GitHub
Desktop for commits, not raw git commands) and prefers lean, low-cost,
automation-first choices over anything requiring an ongoing team or high
infra spend. Prefers being walked through account setup (API keys, bot
creation, hosting) step by step rather than being handed a link and left to
figure it out.
