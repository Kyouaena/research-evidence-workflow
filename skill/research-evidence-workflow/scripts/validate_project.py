#!/usr/bin/env python3
"""Validate research workflow records using only the Python standard library."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ALLOWED_SOURCE_TYPES = {
    "peer_reviewed",
    "preprint",
    "official_document",
    "official_dataset",
    "own_experiment",
}
ALLOWED_CLAIM_TYPES = {"prior_work", "own_result", "method_choice", "limitation"}
REQUIRED_PROTOCOL_KEYS = {
    "protocol_id",
    "version",
    "gate_status",
    "hypotheses",
    "datasets",
    "split_strategy",
    "baselines",
    "primary_metrics",
    "random_seeds",
    "leakage_checks",
    "api_plan",
}
REQUIRED_RUN_KEYS = {
    "run_id",
    "protocol_id",
    "protocol_version",
    "code_revision",
    "dataset_hashes",
    "model_identifiers",
    "parameters",
    "random_seed",
    "raw_output_path",
    "raw_output_hash",
    "status",
    "deviations",
}


def validate_project_brief(path: Path) -> tuple[list[str], dict]:
    data = load_json(path)
    required = {
        "project_id",
        "mode",
        "research_domain",
        "problem_statement",
        "research_question",
        "private_project_path",
        "current_gate",
    }
    errors = [f"project brief: missing key {key}" for key in sorted(required - set(data))]
    if data.get("current_gate") not in {
        "G1_PENDING", "G1_APPROVED", "G2_PENDING", "G2_APPROVED",
        "G3_PENDING", "G3_APPROVED", "G4_PENDING", "G4_APPROVED",
        "G5_PENDING", "G5_APPROVED",
    }:
        errors.append("project brief: invalid current_gate")
    return errors, data


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def load_csv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return list(csv.DictReader(handle))
    except OSError as exc:
        raise ValueError(f"{path}: cannot read CSV: {exc}") from exc


def require_columns(rows: list[dict[str, str]], columns: set[str], label: str) -> list[str]:
    if not rows:
        return [f"{label}: contains no records"]
    missing = columns - set(rows[0])
    return [f"{label}: missing columns {sorted(missing)}"] if missing else []


def validate_evidence(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    rows = load_csv(path)
    errors = require_columns(
        rows,
        {"evidence_id", "source_type", "status", "title", "locator", "verified", "checked_location", "supported_claim"},
        "evidence ledger",
    )
    records: dict[str, dict[str, str]] = {}
    for index, row in enumerate(rows, start=2):
        evidence_id = row.get("evidence_id", "").strip()
        if not evidence_id:
            errors.append(f"evidence ledger row {index}: missing evidence_id")
            continue
        if evidence_id in records:
            errors.append(f"evidence ledger row {index}: duplicate evidence_id {evidence_id}")
        records[evidence_id] = row
        source_type = row.get("source_type", "").strip()
        if source_type not in ALLOWED_SOURCE_TYPES:
            errors.append(f"{evidence_id}: invalid source_type {source_type!r}")
        if not row.get("title", "").strip():
            errors.append(f"{evidence_id}: missing title")
        if not row.get("locator", "").strip():
            errors.append(f"{evidence_id}: missing persistent locator")
        verified = row.get("verified", "").strip().lower()
        if verified not in {"yes", "no"}:
            errors.append(f"{evidence_id}: verified must be yes or no")
        if verified == "yes" and not row.get("checked_location", "").strip():
            errors.append(f"{evidence_id}: verified evidence requires checked_location")
        if verified == "yes" and not row.get("supported_claim", "").strip():
            errors.append(f"{evidence_id}: verified evidence requires supported_claim")
    return errors, records


def validate_claims(path: Path, evidence: dict[str, dict[str, str]], submission: bool = False) -> list[str]:
    rows = load_csv(path)
    errors = require_columns(
        rows,
        {"claim_id", "claim_type", "claim_text", "evidence_ids", "approval_status", "limitations"},
        "claims ledger",
    )
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        claim_id = row.get("claim_id", "").strip()
        if not claim_id:
            errors.append(f"claims ledger row {index}: missing claim_id")
            continue
        if claim_id in seen:
            errors.append(f"claims ledger row {index}: duplicate claim_id {claim_id}")
        seen.add(claim_id)
        claim_type = row.get("claim_type", "").strip()
        if claim_type not in ALLOWED_CLAIM_TYPES:
            errors.append(f"{claim_id}: invalid claim_type {claim_type!r}")
        if submission and row.get("approval_status", "").strip() != "G4_APPROVED":
            errors.append(f"{claim_id}: submission mode requires approval_status G4_APPROVED")
        ids = [item.strip() for item in re.split(r"[;|]", row.get("evidence_ids", "")) if item.strip()]
        if not ids:
            errors.append(f"{claim_id}: requires at least one evidence_id")
        for evidence_id in ids:
            record = evidence.get(evidence_id)
            if record is None:
                errors.append(f"{claim_id}: unknown evidence_id {evidence_id}")
                continue
            if record.get("verified", "").strip().lower() != "yes":
                errors.append(f"{claim_id}: evidence {evidence_id} is not verified")
            if claim_type == "own_result" and record.get("source_type", "").strip() != "own_experiment":
                errors.append(f"{claim_id}: own_result requires own_experiment evidence, not {evidence_id}")
            if claim_type == "prior_work" and record.get("source_type", "").strip() == "own_experiment":
                errors.append(f"{claim_id}: prior_work cannot rely on own_experiment evidence {evidence_id}")
    return errors


def validate_protocol(path: Path) -> tuple[list[str], dict]:
    data = load_json(path)
    errors = [f"experiment protocol: missing key {key}" for key in sorted(REQUIRED_PROTOCOL_KEYS - set(data))]
    if data.get("gate_status") not in {"G2_PENDING", "G2_APPROVED"}:
        errors.append("experiment protocol: gate_status must be G2_PENDING or G2_APPROVED")
    if data.get("gate_status") == "G2_APPROVED":
        for key in ("hypotheses", "datasets", "baselines", "primary_metrics", "random_seeds", "leakage_checks"):
            if not data.get(key):
                errors.append(f"experiment protocol: approved protocol requires non-empty {key}")
        if not str(data.get("split_strategy", "")).strip():
            errors.append("experiment protocol: approved protocol requires split_strategy")
    api_plan = data.get("api_plan", {})
    if api_plan and api_plan.get("gate_status") not in {"G3_PENDING", "G3_APPROVED"}:
        errors.append("experiment protocol: api_plan gate_status must be G3_PENDING or G3_APPROVED")
    return errors, data


def validate_run_manifest(path: Path) -> tuple[list[str], dict]:
    data = load_json(path)
    errors = [f"run manifest: missing key {key}" for key in sorted(REQUIRED_RUN_KEYS - set(data))]
    if data.get("status") == "completed":
        for key in ("code_revision", "dataset_hashes", "model_identifiers", "raw_output_path", "raw_output_hash"):
            if not data.get(key):
                errors.append(f"run manifest: completed run requires {key}")
        if data.get("random_seed") is None:
            errors.append("run manifest: completed run requires random_seed or an explicit documented non-deterministic policy")
    return errors, data


def validate_bibtex(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"BibTeX: cannot read {path}: {exc}"]
    errors: list[str] = []
    entries = re.findall(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, flags=re.DOTALL)
    if not entries:
        return ["BibTeX: no parseable entries found"]
    seen: set[str] = set()
    for entry_type, key, body in entries:
        if key in seen:
            errors.append(f"BibTeX: duplicate key {key}")
        seen.add(key)
        lower = body.lower()
        for field in ("title", "author", "year"):
            if not re.search(rf"\b{field}\s*=", lower):
                errors.append(f"BibTeX {key}: missing {field}")
        if entry_type.lower() != "misc" and not any(token in lower for token in ("doi", "url", "eprint")):
            errors.append(f"BibTeX {key}: missing DOI, URL, or eprint locator")
    return errors


def validate_project(project: Path, submission: bool = False) -> list[str]:
    files = {
        "brief": project / "project_brief.json",
        "evidence": project / "evidence_ledger.csv",
        "claims": project / "claims_ledger.csv",
        "protocol": project / "experiment_protocol.json",
        "run": project / "run_manifest.json",
        "bib": project / "references.bib",
    }
    missing = [f"missing required file: {path}" for path in files.values() if not path.is_file()]
    if missing:
        return missing
    errors, brief = validate_project_brief(files["brief"])
    evidence_errors, evidence = validate_evidence(files["evidence"])
    errors.extend(evidence_errors)
    errors.extend(validate_claims(files["claims"], evidence, submission=submission))
    protocol_errors, protocol = validate_protocol(files["protocol"])
    errors.extend(protocol_errors)
    run_errors, run = validate_run_manifest(files["run"])
    errors.extend(run_errors)
    errors.extend(validate_bibtex(files["bib"]))
    if run.get("status") == "completed":
        if protocol.get("gate_status") != "G2_APPROVED":
            errors.append("cross-check: completed run requires G2_APPROVED protocol")
        if run.get("protocol_id") != protocol.get("protocol_id") or run.get("protocol_version") != protocol.get("version"):
            errors.append("cross-check: run manifest protocol ID/version does not match experiment protocol")
        api_plan = protocol.get("api_plan", {})
        if api_plan.get("models") and api_plan.get("gate_status") != "G3_APPROVED":
            errors.append("cross-check: completed API run requires G3_APPROVED api_plan")
    if submission and brief.get("current_gate") not in {"G5_PENDING", "G5_APPROVED"}:
        errors.append("cross-check: submission mode requires project current_gate G5_PENDING or G5_APPROVED")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True, help="Private project directory containing workflow records")
    parser.add_argument("--submission", action="store_true", help="Require G4-approved claims and G5 project state")
    args = parser.parse_args()
    errors = validate_project(args.project, submission=args.submission)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED: schemas and evidence traceability are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
