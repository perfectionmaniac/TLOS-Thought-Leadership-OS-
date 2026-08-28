#!/usr/bin/env python3
"""
TLOS command-line entry point.

Usage:
    python main.py new "the idea you want to turn into content"
    python main.py new "the idea" --context "any extra founder context"

This runs the full Content Orchestrator pipeline end to end (research ->
positioning -> strategy -> founder voice -> writing -> review -> publishing
package) and saves the result under reports/generated/.
"""

from __future__ import annotations

import argparse
import json
import sys

from tlos_engine.pipeline import run_pipeline
from tlos_engine.linkedin_ingest import build_linkedin_intelligence_input
from tlos_engine.llm_clients import call_claude
from tlos_engine.specs import build_system_prompt


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the TLOS content pipeline.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Turn an idea into a reviewed content package.")
    new_parser.add_argument("idea", help="The raw idea, observation, or topic to develop.")
    new_parser.add_argument(
        "--context", default="", help="Optional extra founder context for this idea."
    )

    li_parser = subparsers.add_parser(
        "analyze-linkedin", help="Run the LinkedIn Data Analysis Engine on your exports."
    )
    li_parser.add_argument("--audience", help="Path to the LinkedIn Audience Analytics .xlsx export.")
    li_parser.add_argument("--content", help="Path to the LinkedIn Content Analytics .xlsx export.")

    args = parser.parse_args()

    if args.command == "new":
        result = run_pipeline(args.idea, founder_context=args.context)
        print("\n" + "=" * 60)
        print(f"Final status: {result.final_status}")
        print(f"Full output saved to: {result.output_path}")
        print("=" * 60)
        if result.final_status == "approved":
            publishing = result.steps.get("publishing", {})
            print("\nReady-to-review content:\n")
            print(json.dumps(publishing, indent=2))
        else:
            print(
                "\nThe draft was not approved by the Review Engine after "
                f"{1} revision round(s). Open the saved JSON file to see "
                "the review feedback and decide whether to revise manually "
                "or re-run with a sharper idea/context."
            )
        return

    if args.command == "analyze-linkedin":
        if not args.audience and not args.content:
            print("Provide at least --audience or --content (paths to your .xlsx exports).")
            sys.exit(1)
        print("Reading LinkedIn export(s)...")
        intelligence_input = build_linkedin_intelligence_input(args.audience, args.content)
        print("Running LinkedIn Data Analysis Engine...")
        system_prompt = build_system_prompt("linkedin_data_analysis_engine")
        analysis = call_claude(system_prompt, json.dumps(intelligence_input), max_tokens=8192)
        out_path = "../reports/generated/linkedin_analysis_latest.json"
        import pathlib

        pathlib.Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(out_path).write_text(json.dumps(analysis, indent=2), encoding="utf-8")
        print(f"\nSaved analysis to {out_path}\n")
        print(json.dumps(analysis, indent=2))
        return

    sys.exit(1)


if __name__ == "__main__":
    main()
