#!/usr/bin/env python3
import argparse
import json
from agent_eval import load_scenarios, run_scenario, score, generate_report


def main():
    parser = argparse.ArgumentParser(description="Agent Eval Harness")
    sub = parser.add_subparsers(dest="cmd")

    run_p = sub.add_parser("run", help="Run evaluation suite")
    run_p.add_argument("--suite", required=True, help="Directory of YAML scenario files")
    run_p.add_argument("--model", default="gpt-4o", help="LLM model to test")
    run_p.add_argument("--output", default=None, help="Output file (.json or .html)")
    run_p.add_argument("--dry-run", action="store_true", help="Skip LLM calls, use mock output")

    args = parser.parse_args()

    if args.cmd == "run":
        scenarios = load_scenarios(args.suite)
        print(f"Loaded {len(scenarios)} scenarios from {args.suite}")
        results = []
        for s in scenarios:
            actual = "[dry-run]" if args.dry_run else run_scenario(s, args.model)
            scoring_cfg = s.get("scoring", {})
            result = score(actual, s["expected"], scoring_cfg.get("method", "semantic_similarity"), scoring_cfg.get("threshold", 0.85))
            result.update({"id": s["id"], "input": s["input"], "expected": s["expected"], "actual": actual})
            status = "✅ PASS" if result["passed"] else "❌ FAIL"
            print(f"  {status} {s['id']} (score: {result.get('score', '?')})")
            results.append(result)

        report = generate_report(results, args.output)
        print(f"\nResults: {report['summary']['passed']}/{report['summary']['total']} passed ({report['summary']['pass_rate']*100:.1f}%)")
        if args.output:
            print(f"Report saved to {args.output}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
