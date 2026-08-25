# Approval gates

## Approval syntax

Request approval with a named gate and version, for example:

`Approve G2 for experiment_protocol.json version 1.2?`

Accept explicit responses such as:

- `APPROVE G2`
- `Approve G2 version 1.2`
- `I approve the G2 experiment protocol shown above.`

Do not accept these as approval:

- `continue`
- `looks interesting`
- `try it`
- silence or absence of objection
- approval of a different version

## Gate-specific checks

### G1 research question

- Question is falsifiable.
- Scope and unit of analysis are defined.
- Claimed novelty is provisional until literature verification.
- Success and rejection conditions are stated.

### G2 experiment protocol

- Data sources and licenses are recorded.
- Train, development, and test boundaries are frozen.
- Primary metrics and statistical methods are selected before test inspection.
- Baselines and ablations are justified.
- Leakage, confounding, and exclusion rules are explicit.

### G3 API and runtime

- Provider, model, version/date, and parameters are named.
- Estimated calls, tokens, cost range, and runtime are shown.
- Private information exposure is described.
- Retry and spending limits are defined.

### G4 results and claims

- Metrics are recomputed from raw outputs.
- Deviations and failed runs are disclosed.
- Uncertainty and limitations accompany point estimates.
- Claims do not exceed the evidence.

### G5 manuscript

- Every substantive claim maps to a verified citation or approved result.
- Prior work and author contributions are clearly separated.
- BibTeX identifiers have been checked against original records.
- AI assistance is disclosed according to applicable rules.

## Revocation

Allow the user to revoke a gate. Stop downstream work, mark dependent artifacts stale, and identify what must be repeated.

