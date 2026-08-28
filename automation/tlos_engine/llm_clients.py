"""
Thin wrappers around the two model providers TLOS uses:

- Claude (Anthropic) — orchestration, positioning, strategy, writing, review.
- Perplexity — grounded/live web research for the Research Analyst step.

Both wrappers return plain Python dicts (parsed from the model's JSON
response), so the pipeline code never has to deal with raw API responses.
"""

from __future__ import annotations

import json
import requests

from .config import Config

# NOTE on Perplexity: as of this writing (Aug 2026), Perplexity is
# deprecating the Sonar API in favor of a new Agent API, with Sonar support
# ending September 2026. This wrapper calls the OpenAI-compatible
# chat/completions endpoint, which is the stable integration path Perplexity
# documents for now. Before going live, check https://docs.perplexity.ai for
# the current recommended endpoint/model name and update PERPLEXITY_MODEL
# and PERPLEXITY_ENDPOINT below if they've changed.
PERPLEXITY_ENDPOINT = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = "sonar-pro"


class LLMError(RuntimeError):
    pass


def _extract_json(raw_text: str) -> dict:
    """
    Parse a model reply as JSON. Falls back to extracting the first
    {...} block if the model wrapped it in prose or a code fence despite
    instructions not to.
    """
    raw_text = raw_text.strip()
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        pass

    start = raw_text.find("{")
    end = raw_text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(raw_text[start : end + 1])
        except json.JSONDecodeError as exc:
            raise LLMError(
                f"Model reply was not valid JSON, even after extraction.\n"
                f"Raw reply:\n{raw_text[:2000]}"
            ) from exc

    raise LLMError(f"Model reply contained no JSON object.\nRaw reply:\n{raw_text[:2000]}")


def call_claude(system_prompt: str, user_message: str, *, max_tokens: int = 4096) -> dict:
    """Call Claude with a system prompt (a TLOS capability spec) and a user
    message (the structured context handed off from the previous pipeline
    step), returning the parsed JSON response."""
    import anthropic

    client = anthropic.Anthropic(api_key=Config.require_anthropic())
    response = client.messages.create(
        model=Config.CLAUDE_MODEL,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    raw_text = "".join(
        block.text for block in response.content if getattr(block, "type", None) == "text"
    )
    return _extract_json(raw_text)


def call_perplexity_research(query: str) -> dict:
    """
    Call Perplexity for grounded, live web research. Returns a dict with
    'answer' (the synthesized text) and 'citations' (list of source URLs,
    when the API provides them).
    """
    headers = {
        "Authorization": f"Bearer {Config.require_perplexity()}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": PERPLEXITY_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a research assistant. Answer with current, "
                    "well-sourced information. Be concise and factual."
                ),
            },
            {"role": "user", "content": query},
        ],
    }
    resp = requests.post(PERPLEXITY_ENDPOINT, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        raise LLMError(f"Perplexity API error {resp.status_code}: {resp.text[:1000]}")
    data = resp.json()
    answer = data["choices"][0]["message"]["content"]
    citations = data.get("citations", [])
    return {"answer": answer, "citations": citations}
