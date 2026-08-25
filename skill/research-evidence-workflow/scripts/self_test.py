#!/usr/bin/env python3
"""Run offline synthetic tests for validate_project.py."""

from __future__ import annotations

import csv
import json
import tempfile
from pathlib import Path

from validate_project import validate_project


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_valid_project(root: Path) -> None:
    brief = {
        "project_id": "synthetic", "mode": "idea_or_existing_project",
        "research_domain": "synthetic", "problem_statement": "synthetic",
        "research_question": "synthetic?", "private_project_path": "/private/synthetic",
        "current_gate": "G4_PENDING",
    }
    (root / "project_brief.json").write_text(json.dumps(brief), encoding="utf-8")
    write_csv(
        root / "evidence_ledger.csv",
        ["evidence_id", "source_type", "status", "title", "authors", "year", "venue", "locator", "verified", "checked_location", "supported_claim", "limitations", "notes"],
        [{"evidence_id": "E001", "source_type": "peer_reviewed", "status": "published", "title": "Synthetic Study", "authors": "A. Author", "year": "2025", "venue": "Test Venue", "locator": "https://doi.org/10.0000/synthetic", "verified": "yes", "checked_location": "p. 3", "supported_claim": "Synthetic bounded claim", "limitations": "Synthetic test only", "notes": ""}],
    )
    write_csv(
        root / "claims_ledger.csv",
        ["claim_id", "claim_type", "claim_text", "evidence_ids", "manuscript_location", "approval_status", "limitations", "notes"],
        [{"claim_id": "C001", "claim_type": "prior_work", "claim_text": "Synthetic bounded claim", "evidence_ids": "E001", "manuscript_location": "Related Work", "approval_status": "draft", "limitations": "Synthetic", "notes": ""}],
    )
    protocol = {
        "protocol_id": "P001", "version": "1.0", "gate_status": "G2_APPROVED",
        "hypotheses": ["H1"], "datasets": ["synthetic"], "split_strategy": "chronological",
        "baselines": ["naive"], "primary_metrics": ["MAE"], "random_seeds": [1],
        "leakage_checks": ["timestamp audit"], "api_plan": {"gate_status": "G3_PENDING"},
    }
    (root / "experiment_protocol.json").write_text(json.dumps(protocol), encoding="utf-8")
    run = {
        "run_id": "R001", "protocol_id": "P001", "protocol_version": "1.0",
        "code_revision": "abc123", "dataset_hashes": {"synthetic": "hash"},
        "model_identifiers": ["local-test-model"], "parameters": {}, "random_seed": 1,
        "raw_output_path": "private/raw.json", "raw_output_hash": "hash", "status": "completed",
        "deviations": [],
    }
    (root / "run_manifest.json").write_text(json.dumps(run), encoding="utf-8")
    (root / "references.bib").write_text(
        "@article{synthetic2025,\n  author={A. Author},\n  title={Synthetic Study},\n  year={2025},\n  doi={10.0000/synthetic}\n}\n",
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        build_valid_project(root)
        errors = validate_project(root)
        assert not errors, f"valid project failed: {errors}"

        claims_path = root / "claims_ledger.csv"
        rows = list(csv.DictReader(claims_path.open(encoding="utf-8")))
        rows[0]["claim_type"] = "own_result"
        write_csv(claims_path, list(rows[0]), rows)
        errors = validate_project(root)
        assert any("own_result requires own_experiment" in error for error in errors), errors

        build_valid_project(root)
        errors = validate_project(root, submission=True)
        assert any("submission mode requires approval_status G4_APPROVED" in error for error in errors), errors
        assert any("submission mode requires project current_gate" in error for error in errors), errors

    print("SELF-TEST PASSED: valid records accepted and ownership violation rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
