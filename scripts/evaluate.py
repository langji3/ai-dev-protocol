"""Export unbiased scenarios and score recorded actions; never invokes a model or external API."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cases():
    return json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))["cases"]


def canonical_route(route):
    aliases = {"discussion": "Discussion Only", "quick_fix": "Quick Fix Path",
               "full_development_flow": "Full Development Flow",
               "merge-back": "Full Development Flow", "recovery": "Full Development Flow"}
    if isinstance(route, str) and route.startswith("Apifox Standalone / "):
        return "Apifox Standalone"
    return aliases.get(route, route)


def evaluate(record, artifact_root=None):
    known = {c["id"]: c for c in cases()}
    if record.get("mode") not in {"independent-simulation", "live"}:
        raise ValueError("Record must distinguish independent-simulation from live execution")
    for key in ("tool", "toolVersion", "pluginVersion", "date"):
        if not record.get(key):
            raise ValueError(f"Missing run metadata: {key}")
    results = []
    seen = set()
    for item in record.get("cases", []):
        ident = item.get("id")
        if ident not in known or ident in seen:
            raise ValueError(f"Unknown or duplicate case: {ident}")
        seen.add(ident)
        expected = known[ident]["expect"]
        actions = set(item.get("actions", []))
        errors = []
        if canonical_route(item.get("route")) != expected["route"]:
            errors.append("wrong route")
        errors += [f"missing action: {a}" for a in expected["required"] if a not in actions]
        for choices in expected.get("requiredAny", []):
            if not actions.intersection(choices):
                errors.append(f"missing action from alternatives: {choices}")
        errors += [f"forbidden action: {a}" for a in expected["forbidden"] if a in actions]
        if not item.get("evidence"):
            errors.append("missing action/state evidence")
        errors += item.get("reviewIssues", [])
        if record["mode"] == "live":
            artifacts = item.get("artifacts")
            if not isinstance(artifacts, list) or not artifacts or artifact_root is None:
                errors.append("live case requires verifiable artifact files")
            else:
                import hashlib
                base = Path(artifact_root).resolve()
                for artifact in artifacts:
                    if not isinstance(artifact, dict) or not isinstance(artifact.get("path"), str):
                        errors.append("invalid artifact descriptor")
                        continue
                    path = (base / artifact["path"]).resolve()
                    if (not path.is_relative_to(base) or not path.is_file()
                            or hashlib.sha256(path.read_bytes()).hexdigest() != artifact.get("sha256")):
                        errors.append("missing, escaping or changed artifact")
        results.append({"id": ident, "passed": not errors, "errors": errors})
    unverified = sorted(set(known) - seen)
    return {"mode": record["mode"], "results": results, "unverified": unverified,
            "submittedPassed": bool(results) and all(x["passed"] for x in results),
            "passed": bool(results) and not unverified and all(x["passed"] for x in results)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    prompt = sub.add_parser("prompt")
    prompt.add_argument("id")
    score = sub.add_parser("score")
    score.add_argument("record", type=Path)
    args = parser.parse_args()
    if args.command == "list":
        print("\n".join(c["id"] for c in cases()))
    elif args.command == "prompt":
        case = next((c for c in cases() if c["id"] == args.id), None)
        if case is None:
            parser.error("Unknown scenario")
        # Expectations are intentionally excluded from evaluator input.
        print(json.dumps({k: v for k, v in case.items() if k != "expect"}, ensure_ascii=False, indent=2))
    else:
        result = evaluate(json.loads(args.record.read_text(encoding="utf-8")), args.record.parent)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["passed"] else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
