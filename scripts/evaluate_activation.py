#!/usr/bin/env python3
"""Prepare a host evaluation and score recorded observations, never simulate one."""
import argparse
import hashlib
import json
from pathlib import Path
import re

from validate_distribution import Invalid, local_path, read_json, require, validate


def plan(root):
    distribution = validate(root)
    cases = read_json(root / "assurance/activation-cases.json")["cases"]
    return {"schema_version": 1, "distribution_sha256": distribution["distribution_sha256"],
            "suite_sha256": hashlib.sha256((root / "assurance/activation-cases.json").read_bytes()).hexdigest(),
            "plugin_version": distribution["version"], "host": "", "model": "", "reviewer": "",
            "candidate_sha": "", "observed_at": "", "cases": [
                {"id": case["id"], "prompt": case["prompt"], "activated_skills": None,
                 "trace": {"path": "", "sha256": ""},
                 "response": {"path": "", "sha256": ""},
                 "activation_evidence": {},
                 "review": {key: {"passed": None, "excerpt": ""}
                            for key in case["review_criteria"]}}
                for case in cases]}


def artifact(base, record):
    require(isinstance(record, dict), "missing evidence artifact")
    path = local_path(base, record.get("path"), base)
    content = path.read_bytes()
    require(hashlib.sha256(content).hexdigest() == record.get("sha256"), "evidence artifact digest mismatch")
    return content.decode("utf-8")


def score(root, evidence_path):
    distribution = validate(root)
    evidence = read_json(evidence_path)
    require(evidence.get("schema_version") == 1, "unsupported observation contract")
    require(evidence.get("distribution_sha256") == distribution["distribution_sha256"], "stale distribution evidence")
    require(evidence.get("suite_sha256") == hashlib.sha256((root / "assurance/activation-cases.json").read_bytes()).hexdigest(), "stale activation suite evidence")
    require(evidence.get("plugin_version") == distribution["version"], "stale version evidence")
    for key in ["host", "model", "reviewer", "observed_at"]:
        require(isinstance(evidence.get(key), str) and evidence[key].strip(), f"missing provenance: {key}")
    require(re.fullmatch(r"[a-f0-9]{40}", evidence.get("candidate_sha", "")), "missing full candidate SHA")
    cases = read_json(root / "assurance/activation-cases.json")["cases"]
    records = evidence.get("cases")
    require(isinstance(records, list) and len(records) == len(cases), "incomplete evidence suite")
    require(len({r["id"] for r in records}) == len(records), "duplicate case observations")
    by_id = {r["id"]: r for r in records}
    require(set(by_id) == {c["id"] for c in cases}, "observation case IDs do not match suite")
    skills = set(read_json(root / "assurance/distribution.json")["skills"])
    for case in cases:
        record = by_id[case["id"]]
        require(record.get("prompt") == case["prompt"], f"prompt changed: {case['id']}")
        activated = record.get("activated_skills")
        require(isinstance(activated, list) and len(activated) == len(set(activated)), "activation must be an observed unique list")
        require(set(activated) <= skills, "unknown activated skill")
        require(set(case["required_skills"]) <= set(activated), f"required activation missing: {case['id']}")
        require(not set(case["forbidden_skills"]) & set(activated), f"forbidden activation: {case['id']}")
        require(not (case["forbid_all"] and activated), f"plugin overactivated: {case['id']}")
        trace = artifact(evidence_path.parent, record.get("trace"))
        response = artifact(evidence_path.parent, record.get("response"))
        require(bool(trace.strip()) and bool(response.strip()), "empty host evidence")
        anchors = record.get("activation_evidence", {})
        require(set(anchors) == set(activated), "every observed skill needs a trace anchor")
        for anchor in anchors.values():
            require(isinstance(anchor, str) and anchor.strip() and anchor in trace, "activation anchor absent from trace")
        review = record.get("review", {})
        require(set(review) == set(case["review_criteria"]), "incomplete rubric review")
        for assessment in review.values():
            require(assessment.get("passed") is True, f"behavior criterion failed or unreviewed: {case['id']}")
            excerpt = assessment.get("excerpt", "")
            require(isinstance(excerpt, str) and excerpt.strip() and (excerpt in response or excerpt in trace),
                    "review excerpt absent from host evidence")
    return {"status": "recorded evidence accepted", "cases": len(cases),
            "distribution_sha256": distribution["distribution_sha256"],
            "scope": "activation set, provenance, artifact digests and recorded rubric verdicts checked; human judgments retained"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("plan")
    scoring = sub.add_parser("score")
    scoring.add_argument("evidence", type=Path)
    args = parser.parse_args()
    try:
        result = plan(args.root) if args.command == "plan" else score(args.root, args.evidence.resolve())
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (Invalid, KeyError, TypeError, OSError, ValueError) as error:
        parser.exit(1, f"activation evaluation failed: {error}\n")


if __name__ == "__main__":
    main()
