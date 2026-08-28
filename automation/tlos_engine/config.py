"""
Central configuration for the TLOS engine.

Loads secrets and paths from environment variables / a local .env file
(never from anywhere that gets committed to GitHub).
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the automation/ directory regardless of current working dir.
_THIS_DIR = Path(__file__).resolve().parent.parent
load_dotenv(_THIS_DIR / ".env")


class Config:
    ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY")
    PERPLEXITY_API_KEY: str | None = os.getenv("PERPLEXITY_API_KEY")
    TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_OWNER_CHAT_ID: str | None = os.getenv("TELEGRAM_OWNER_CHAT_ID")

    # Anthropic model used for orchestration, writing, and review steps.
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5")

    # Repo root — where skills/, workflows/, engines/, reports/, knowledge/ live.
    REPO_ROOT: Path = Path(
        os.getenv("TLOS_REPO_ROOT", str(_THIS_DIR.parent))
    ).resolve()

    @classmethod
    def require_anthropic(cls) -> str:
        if not cls.ANTHROPIC_API_KEY:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Copy automation/.env.example to "
                "automation/.env and fill in your Claude API key."
            )
        return cls.ANTHROPIC_API_KEY

    @classmethod
    def require_perplexity(cls) -> str:
        if not cls.PERPLEXITY_API_KEY:
            raise RuntimeError(
                "PERPLEXITY_API_KEY is not set. Copy automation/.env.example to "
                "automation/.env and fill in your Perplexity API key."
            )
        return cls.PERPLEXITY_API_KEY
