# Workflow and deliverables

## Stage map

| Stage | Required input | Required output | Exit condition |
|---|---|---|---|
| 0 Intake | Idea or private project | Project brief and artifact inventory | Unknowns are explicit |
| 1 Question | Project brief | Falsifiable question and scope | G1 approval |
| 2 Evidence | Approved question | Verified evidence ledger and BibTeX candidates | Evidence gaps reported |
| 3 Design | Evidence ledger | Frozen experiment protocol | G2 approval |
| 4 Cost | Protocol and API plan | Cost, runtime, privacy estimate | G3 approval |
| 5 Execute | Approved protocol | Raw outputs and run manifests | Runs reproducible |
| 6 Audit | Raw outputs | Recomputed results and claims ledger | G4 approval |
| 7 Write | Approved claims | LaTeX draft, BibTeX, disclosure log | G5 approval |

## State rules

- Keep discovery, verification, execution, interpretation, and writing as separate states.
- Move an artifact forward only when its required fields are complete.
- Version protocols and manifests. Never overwrite the reason for a change.
- Preserve raw outputs as immutable. Generate derived tables in a separate directory.
- Record a failed run as evidence about execution, not as a result supporting a claim.

## Gate packets

Prepare a compact packet at each gate:

- Decision requested.
- Exact artifact versions.
- Known evidence.
- Open uncertainties.
- Costs and risks.
- Actions that become authorized after approval.
- Actions that remain prohibited.

## Existing-project mode

When joining an existing project, reconstruct provenance before recommending changes:

1. Map manuscript claims to tables, tables to scripts, and scripts to raw outputs.
2. Identify conflicts in dataset counts, model versions, splits, prompts, thresholds, and metrics.
3. Mark unresolved conflicts as blockers.
4. Avoid treating the manuscript as ground truth for missing experiment values.

