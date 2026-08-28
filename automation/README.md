# TLOS Automation Engine

This is the real, running implementation of the TLOS Content Orchestrator
pipeline described in `workflows/content_orchestrator.md` and the specialist
specs in `skills/`, `workflows/`, and `engines/`. It's a Python CLI for now —
a Telegram bot and a weekly scheduler come next, once this core engine is
proven end to end.

## What it does right now

Given a raw idea, it runs the idea through six real specialist steps —
Research, Positioning, Strategy, Founder Voice, Writing, Review — with up to
one revision round if the Review Engine doesn't approve the first draft. If
approved, it prepares a publishing package. Every step is a real call to
Claude (and, for research, optionally Perplexity), using the actual spec
files in this repo as instructions — not a rewritten or simplified version
of them.

This is intentionally a straight-through MVP path. The full orchestrator
spec describes richer routing (a 6-question strategic gate before starting,
rejected drafts going back to strategy rather than just writing, etc.) —
that's the natural next iteration once this simpler path is proven on real
content.

## Setup

1. **Install dependencies** (from inside this `automation/` folder):
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a Claude (Anthropic) API key:**
   - Go to https://console.anthropic.com and sign up / log in.
   - Go to "API Keys" in the left sidebar, click "Create Key".
   - Copy the key (starts with `sk-ant-...`) — you won't be able to see it again.
   - Note: this is pay-as-you-go, billed separately from any Claude.ai subscription. Add a small amount of credit ($5-10 is plenty to start) under "Billing".

3. **Get a Perplexity API key** (optional for now — the pipeline works without it, just with less grounded live research):
   - Go to https://www.perplexity.ai/settings/api and sign up / log in.
   - Generate an API key, copy it.
   - Add a small amount of credit under billing.

4. **Set up your `.env` file:**
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and paste in your keys:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   PERPLEXITY_API_KEY=pplx-...
   ```
   Never commit `.env` to GitHub — it's already covered by `.gitignore`.

## Running it

From inside `automation/`:

```bash
python main.py new "why most B2B founders undersell their product's actual moat"
```

Optionally add extra context:

```bash
python main.py new "your idea" --context "I want to tie this to a recent partnership announcement"
```

It will print progress for each specialist step as it runs, then save the
full structured result to `../reports/generated/<timestamp>-<slug>.json` and
print the final publishing package (if approved) or the review feedback (if
not) to the terminal.

## What this does NOT do yet

- It does not post to LinkedIn automatically — LinkedIn has no reliable API
  for a personal profile's posting/analytics, so publishing stays a
  copy-paste-to-LinkedIn step by design, with the Publishing Workflow output
  giving you the exact text, format, and timing recommendation.
- It does not yet ingest your LinkedIn analytics exports automatically —
  that's `tlos_engine/linkedin_ingest.py`, built but not yet wired into the
  CLI (next task).
- It does not run on a schedule or have a chat interface yet — see the
  project task list for what's next.
