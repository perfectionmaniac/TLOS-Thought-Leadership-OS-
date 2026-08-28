"""
Loads the actual approved Markdown specification files from this repository
and turns them into LLM system prompts.

This is the bridge between "the specs" (skills/, workflows/, engines/) and
"the engine" (this Python package). If you edit a spec file and re-run the
pipeline, the new spec text is what the model sees — the code does not cache
or duplicate the spec content anywhere else.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from .config import Config

# Registry: logical capability name -> spec file(s) relative to repo root.
# A capability can be backed by more than one file (e.g. the orchestrator
# references several engines); all listed files are concatenated in order.
SPEC_REGISTRY: dict[str, list[str]] = {
    "operating_principles": [
        "skills/001-ai-operating-principles.md",
        "skills/008-quality-assurance.md",
        "skills/009-output-formatting.md",
    ],
    "research_analyst": ["skills/Research_Analyst.md"],
    "positioning_expert": ["skills/Positioning_Expert.md"],
    "chief_content_strategist": ["skills/Chief_Content_Strategist.md"],
    "founder_voice_engine": ["skills/Founder_Voice_Engine.md"],
    "writing_engine": ["workflows/Writing Engine.md", "skills/LinkedIn_Writer.md"],
    "review_engine": ["workflows/review-engine.md"],
    "publishing_workflow": ["workflows/publishing-workflow.md"],
    "performance_analytics": ["workflows/Performance-Analytics.md"],
    "knowledge_repository": ["knowledge/Knowledge Repository.md"],
    "linkedin_data_analysis_engine": ["engines/linkedin_data_analysis_engine.md"],
    "linkedin_growth_os": ["workflows/linkedin_growth_os.md"],
    "content_orchestrator": ["workflows/content_orchestrator.md"],
}


def _strip_frontmatter(text: str) -> str:
    """Remove a leading YAML frontmatter block (--- ... ---) if present."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


@lru_cache(maxsize=None)
def load_spec(name: str) -> str:
    """Load and concatenate the Markdown spec file(s) for a capability."""
    if name not in SPEC_REGISTRY:
        raise KeyError(
            f"Unknown spec '{name}'. Known specs: {sorted(SPEC_REGISTRY)}"
        )
    parts = []
    for rel_path in SPEC_REGISTRY[name]:
        full_path = Config.REPO_ROOT / rel_path
        if not full_path.exists():
            raise FileNotFoundError(
                f"Spec file for '{name}' not found at {full_path}. "
                f"Check TLOS_REPO_ROOT in your .env."
            )
        parts.append(_strip_frontmatter(full_path.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(parts)


def build_system_prompt(capability: str, *, include_operating_principles: bool = True) -> str:
    """
    Build the full system prompt for one pipeline step: the shared Universal
    AI Operating Layer principles (SKILL-001/008/009), followed by the
    specific capability's own spec.
    """
    sections = []
    if include_operating_principles:
        sections.append(
            "# Universal AI Operating Layer — Governing Principles\n\n"
            + load_spec("operating_principles")
        )
    sections.append(f"# Capability Specification\n\n{load_spec(capability)}")
    sections.append(
        "\n\n# Output Contract\n\n"
        "Respond with a single JSON object only — no prose before or after it, "
        "no markdown code fences. The calling code will parse your entire "
        "reply as JSON, so invalid JSON will break the pipeline."
    )
    return "\n\n".join(sections)
