---
name: research-evidence-workflow
description: Manage an approval-gated, evidence-first doctoral research workflow from topic formulation and literature verification through Python/API experiments, result auditing, and LaTeX/BibTeX manuscript drafting. Use for LLM or Agent safety evaluations, financial time-series forecasting, system prototypes, ablation studies, reproducibility reviews, citation audits, or research writing where claims must remain traceable and academic integrity must be enforced. Also trigger for natural Chinese requests such as “我要开始做大研究了”, “开始一个新研究”, “帮我规划博士研究”, “进入研究证据模式”, “帮我设计并冻结实验”, “审计我的实验结果”, or “从证据开始写论文”.
---

# Research Evidence Workflow

Treat research assistance as controlled evidence production, not autonomous authorship.

## Recognize activation phrases

Treat the following phrases and close paraphrases as explicit requests to start or resume this workflow:

- `我要开始做大研究了`: start at Stage 0 and establish the private project context.
- `开始一个新研究`: start with idea intake and research-question formulation.
- `帮我规划博士研究`: inventory the current doctoral research state before proposing a plan.
- `进入研究证据模式`: enforce evidence-ledger and approval-gate behavior immediately.
- `帮我设计并冻结实验`: prepare the G2 experiment protocol without running it.
- `审计我的实验结果`: start at Stage 6 and reconstruct provenance before interpreting results.
- `从证据开始写论文`: verify G4-approved claims before drafting any manuscript text.
- `继续我的大研究`: resume from the latest explicitly approved gate; never assume an unrecorded approval.

Ask for only the missing context required by the selected entry point. Preserve all approval and integrity rules regardless of the activation phrase.

## Start every project

1. Identify the private project directory. Never copy private artifacts into this skill or its public source repository.
2. Copy only the needed templates from `assets/templates/` into the private project directory.
3. Read `references/workflow.md` and `references/approvals.md`.
4. Read the method-specific sections in `references/methods.md`.
5. Read `references/integrity-and-evidence.md` before literature work or result interpretation.
6. Read `references/manuscript.md` before producing LaTeX or BibTeX.
7. Record assumptions, missing inputs, and the current approval state before acting.

## Enforce approval gates

Stop at every gate. Accept approval only when the user explicitly writes `APPROVE G1`, `APPROVE G2`, `APPROVE G3`, `APPROVE G4`, or `APPROVE G5`, or an unambiguous equivalent naming that gate and its artifact.

- G1: approve the research question, scope, and proposed contribution.
- G2: approve the frozen experiment protocol, data split, metrics, baselines, and analysis plan.
- G3: approve the named API models, estimated calls, estimated cost, data exposure, and runtime.
- G4: approve the audited results, anomalies, limitations, and claims supported by them.
- G5: approve the submission-oriented manuscript, citations, and AI-use disclosure.

Do not interpret generic continuation language as gate approval. See `references/approvals.md`.

## Follow the stage workflow

### Stage 0: Intake

- Determine whether the task starts from an idea or an existing project.
- Inventory available papers, code, data, logs, results, LaTeX, and BibTeX without modifying them.
- Populate `project_brief.json`.
- Classify unknown facts as questions, not assumptions.

### Stage 1: Research question

- Convert the idea into a falsifiable question, bounded scope, candidate contributions, and rejection conditions.
- Separate desired contribution from evidence already available.
- Search for novelty only after defining comparison dimensions.
- Present the G1 packet and stop.

### Stage 2: Evidence review

- Discover candidate literature broadly, but cite only verified original records.
- Record each source in `evidence_ledger.csv` with type, status, locator, checked passage, and supported claim.
- Label preprints explicitly and replace them with peer-reviewed versions when available.
- Never create a BibTeX record from model memory alone.
- Report contradictions and missing evidence instead of resolving them by invention.

### Stage 3: Experiment design

- Populate `experiment_protocol.json` before accessing final test outcomes.
- Freeze hypotheses, datasets, splits, baselines, primary metrics, statistical tests, stopping rules, and exclusions.
- Add method-specific leakage and confounding checks.
- Present the G2 packet and stop.

### Stage 4: Cost and execution plan

- Name every external model and exact version when available.
- Estimate calls, tokens, cost range, runtime, and information exposed to the provider.
- Keep credentials in environment variables and never print or store them.
- Present the G3 packet and stop before any paid call or long-running experiment.

### Stage 5: Execute and record

- Run only the approved protocol.
- Save immutable raw outputs before aggregation.
- Populate `run_manifest.json` with code revision, environment, seeds, timestamps, model versions, and output hashes.
- Preserve failures, retries, exclusions, and deviations.
- Treat any protocol deviation as a new version requiring explanation and, when material, renewed G2/G3 approval.

### Stage 6: Audit results

- Recompute metrics from raw outputs.
- Compare tables, figures, narrative numbers, and ledger entries.
- Distinguish confirmatory results from exploratory observations.
- Report null, negative, and contradictory outcomes.
- Populate `claims_ledger.csv`; link every claim to admissible evidence.
- Present the G4 packet and stop.

### Stage 7: Draft manuscript

- Draft LaTeX only from G4-approved claims and verified BibTeX records.
- Attribute prior work and the author's results with unambiguous language.
- Do not imitate source wording; synthesize in original language and cite the source.
- Include limitations, reproducibility details, and AI-use disclosure appropriate to the target venue.
- Present the G5 packet and stop before generating a submission-ready version.

## Validate deterministic records

Run:

```bash
python scripts/validate_project.py --project /path/to/private-project
```

Treat a passing result as schema and traceability validation, not scientific endorsement. Correct every reported error before advancing a gate.

## Refuse integrity violations

Refuse requests to fabricate or backfill results, invent citations, misrepresent another scholar's finding, hide inconvenient runs, tune on final test labels, bypass an approval gate, or expose private research and credentials. Offer a compliant alternative such as marking the value missing, rerunning the experiment, narrowing the claim, or adding a transparent limitation.
