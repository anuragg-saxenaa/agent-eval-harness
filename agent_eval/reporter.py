import json
from datetime import datetime, timezone


def generate_report(results: list[dict], output_path: str = None) -> dict:
    """Generate JSON + HTML report from results."""
    total = len(results)
    passed = sum(1 for r in results if r.get("passed"))
    report = {
        "summary": {"total": total, "passed": passed, "failed": total - passed, "pass_rate": round(passed / total, 4) if total else 0},
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }

    if output_path:
        if output_path.endswith(".json"):
            with open(output_path, "w") as f:
                json.dump(report, f, indent=2)
        elif output_path.endswith(".html"):
            with open(output_path, "w") as f:
                f.write(_html(report))

    return report


def _html(report: dict) -> str:
    s = report["summary"]
    rows = "".join(
        f"<tr><td>{r['id']}</td><td>{r['input'][:60]}</td>"
        f"<td>{'✅' if r['passed'] else '❌'}</td>"
        f"<td>{r.get('score', '')}</td></tr>"
        for r in report["results"]
    )
    return f"""<!DOCTYPE html><html><head><style>
body{{font-family:sans-serif;padding:20px}} table{{border-collapse:collapse;width:100%}}
td,th{{border:1px solid #ddd;padding:8px}} th{{background:#f4f4f4}}
.pass{{color:green}} .fail{{color:red}}
</style></head><body>
<h1>Agent Eval Report</h1>
<p>Pass rate: <strong>{s['pass_rate']*100:.1f}%</strong> ({s['passed']}/{s['total']})</p>
<table><tr><th>ID</th><th>Input</th><th>Pass</th><th>Score</th></tr>{rows}</table>
</body></html>"""
