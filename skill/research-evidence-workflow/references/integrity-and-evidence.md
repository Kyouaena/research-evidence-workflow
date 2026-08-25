# Integrity and evidence policy

## Admissible source classes

Use only these classes in the evidence ledger:

- `peer_reviewed`: published peer-reviewed original research.
- `preprint`: non-peer-reviewed manuscript, always labeled as such.
- `official_document`: official technical documentation, standards, or policy.
- `official_dataset`: official dataset page, card, repository, or release record.
- `own_experiment`: artifact produced by the current approved experiment.

Do not use AI output, a search snippet, a secondary blog, or an unverified citation as evidence. Use reviews to discover original studies, but verify and cite the original study for a substantive empirical claim.

## Verification requirements

Before setting `verified=yes`:

1. Open the original record or full document.
2. Confirm title, authors, year, venue/status, and persistent locator.
3. Locate the passage, table, figure, dataset card, or documentation section supporting the claim.
4. Record limitations and population/context boundaries.
5. Confirm that the wording in the claims ledger does not strengthen the source.

## Ownership rules

- Use `prior_work` for findings from other researchers.
- Use `own_result` only when the evidence type is `own_experiment` and the run passed G2/G3 controls.
- Use `method_choice` for design decisions supported by literature or documentation.
- Use `limitation` for a bounded statement about uncertainty or scope.

Never turn a cited prior result into first-person contribution language. Never reuse source phrasing beyond a necessary short quotation; prefer original synthesis with attribution.

## Prohibited practices

- Citation fabrication or citation laundering.
- Data fabrication, falsification, selective deletion, or target-driven backfilling.
- Test-set tuning, look-ahead leakage, or post-hoc primary metric substitution.
- HARKing without explicit exploratory labeling.
- Duplicate publication or unmarked reuse of substantial prior text/results.
- Undisclosed material AI-generated text, code, figures, or analyses when disclosure is required.

## Uncertainty behavior

When evidence is incomplete, output one of:

- `UNVERIFIED`: a candidate that requires original-source checking.
- `MISSING`: evidence or result does not exist in the supplied artifacts.
- `CONFLICT`: supplied sources disagree.
- `OUT_OF_SCOPE`: the claim exceeds the approved question.

Do not replace these labels with plausible content.

