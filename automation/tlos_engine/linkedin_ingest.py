"""
Parses LinkedIn's exported analytics files (the "Audience Analytics" and
"Content Analytics" .xlsx exports) into a structured summary that feeds the
LinkedIn Data Analysis Engine.

IMPORTANT: this was written before seeing your actual export files, so the
sheet/column handling below is deliberately generic and defensive rather
than hard-coded to exact column names. Once you provide a real export, this
should be recalibrated against its actual sheet names and headers — treat
the numbers this produces as provisional until that happens.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def load_workbook_as_dict(xlsx_path: str | Path) -> dict[str, list[dict]]:
    """Read every sheet in an .xlsx export into {sheet_name: [row_dicts]}."""
    xlsx_path = Path(xlsx_path)
    if not xlsx_path.exists():
        raise FileNotFoundError(f"LinkedIn export not found: {xlsx_path}")

    sheets = pd.read_excel(xlsx_path, sheet_name=None)
    out: dict[str, list[dict]] = {}
    for sheet_name, df in sheets.items():
        df = df.dropna(how="all")
        out[sheet_name] = json.loads(df.to_json(orient="records"))
    return out


def summarize_export(xlsx_path: str | Path, *, max_rows_per_sheet: int = 200) -> dict:
    """
    Produce a compact JSON-safe summary of an export suitable for handing to
    an LLM as context (full raw exports can be too large/noisy to paste
    directly into a prompt).
    """
    sheets = load_workbook_as_dict(xlsx_path)
    summary = {"source_file": str(xlsx_path), "sheets": {}}
    for name, rows in sheets.items():
        summary["sheets"][name] = {
            "row_count": len(rows),
            "columns": list(rows[0].keys()) if rows else [],
            "sample_rows": rows[:max_rows_per_sheet],
        }
    return summary


def build_linkedin_intelligence_input(
    audience_xlsx: str | Path | None = None,
    content_xlsx: str | Path | None = None,
) -> dict:
    """
    Combine the audience + content analytics exports into the structured
    input this repo's engines/linkedin_data_analysis_engine.md expects
    (see inputs/linkedin_intelligence_input.md for the target shape).
    """
    result: dict = {"audience_analytics": None, "content_analytics": None}
    if audience_xlsx:
        result["audience_analytics"] = summarize_export(audience_xlsx)
    if content_xlsx:
        result["content_analytics"] = summarize_export(content_xlsx)
    return result
