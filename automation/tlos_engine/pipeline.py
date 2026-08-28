"""
The Content Orchestrator, implemented as real, running code.

This is a deliberately linear MVP version of workflows/content_orchestrator.md
and workflows/content-production-workflow.md: Research -> Positioning ->
Strategy -> Writing -> Review -> Publishing Package. The full spec describes
a richer decision framework (a 6-question gate before committing resources,
routing rejected drafts back to strategy, etc.) — that richer routing is a
good next iteration once this straight-through path is proven end to end.
Each step still runs the *actual* approved specialist spec, unmodified.

A single run produces one publish-ready content package plus a structured
log of what each specialist decided along the way, saved under
reports/generated/.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .config import Config
from .llm_clients import call_claude, call_perplexity_research
from .specs import build_system_prompt

MAX_REVISION_ROUNDS = 1


@dataclass
class PipelineResult:
    idea: str
    steps: dict = field(default_factory=dict)
    final_status: str = "unknown"
    output_path: str | None = None


def _log(label: str, message: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {label}: {message}")


def _run_step(capability: str, user_message: str, *, label: str) -> dict:
    _log(label, "running...")
    system_prompt = build_system_prompt(capability)
    result = call_claude(system_prompt, user_message)
    _log(label, "done")
    return result


def run_pipeline(idea: str, founder_context: str = "") -> PipelineResult:
    result = PipelineResult(idea=idea)

    # --- Stage 1: Research -----------------------------------------------
    live_research = None
    if Config.PERPLEXITY_API_KEY:
        _log("research", "querying Perplexity for grounded evidence...")
        live_research = call_perplexity_research(idea)
    research_input = json.dumps(
        {
            "idea": idea,
            "founder_context": founder_context,
            "live_web_research": live_research,
        }
    )
    research_output = _run_step(
        "research_analyst", research_input, label="Research Analyst"
    )
    result.steps["research"] = research_output

    # --- Stage 2: Positioning ----------------------------------------------
    positioning_output = _run_step(
        "positioning_expert",
        json.dumps({"idea": idea, "research": research_output}),
        label="Positioning Expert",
    )
    result.steps["positioning"] = positioning_output

    # --- Stage 3: Strategy ---------------------------------------------------
    strategy_output = _run_step(
        "chief_content_strategist",
        json.dumps(
            {"idea": idea, "research": research_output, "positioning": positioning_output}
        ),
        label="Chief Content Strategist",
    )
    result.steps["strategy"] = strategy_output

    # --- Stage 4: Founder voice guidance -------------------------------------
    voice_output = _run_step(
        "founder_voice_engine",
        json.dumps({"idea": idea, "strategy": strategy_output}),
        label="Founder Voice Engine",
    )
    result.steps["founder_voice"] = voice_output

    # --- Stage 5: Writing (with up to MAX_REVISION_ROUNDS revision loop) ----
    draft_output = None
    review_output = None
    for attempt in range(MAX_REVISION_ROUNDS + 1):
        draft_output = _run_step(
            "writing_engine",
            json.dumps(
                {
                    "idea": idea,
                    "research": research_output,
                    "positioning": positioning_output,
                    "strategy": strategy_output,
                    "founder_voice": voice_output,
                    "previous_review": review_output,
                }
            ),
            label=f"Writing Engine (attempt {attempt + 1})",
        )

        review_output = _run_step(
            "review_engine",
            json.dumps(
                {
                    "draft": draft_output,
                    "strategy": strategy_output,
                    "positioning": positioning_output,
                    "founder_voice": voice_output,
                }
            ),
            label=f"Review Engine (attempt {attempt + 1})",
        )
        decision = str(review_output.get("decision", "")).lower()
        if decision == "approved":
            break

    result.steps["draft"] = draft_output
    result.steps["review"] = review_output
    final_decision = str((review_output or {}).get("decision", "unknown")).lower()
    result.final_status = final_decision

    # --- Stage 6: Publishing package (prepared, not auto-posted) -----------
    if final_decision == "approved":
        publishing_output = _run_step(
            "publishing_workflow",
            json.dumps({"draft": draft_output, "review": review_output}),
            label="Publishing Workflow",
        )
        result.steps["publishing"] = publishing_output
    else:
        _log(
            "publishing",
            f"skipped — review decision was '{final_decision}', not 'approved'",
        )

    result.output_path = _save_result(result)
    return result


def _save_result(result: PipelineResult) -> str:
    out_dir = Config.REPO_ROOT / "reports" / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_slug = "".join(c if c.isalnum() else "-" for c in result.idea[:40]).strip("-")
    out_path = out_dir / f"{timestamp}-{safe_slug or 'content'}.json"
    out_path.write_text(
        json.dumps(
            {
                "idea": result.idea,
                "final_status": result.final_status,
                "steps": result.steps,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return str(out_path)
