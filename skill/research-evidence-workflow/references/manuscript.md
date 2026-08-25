# LaTeX, BibTeX, and manuscript controls

## Drafting order

1. Freeze G4 claims.
2. Map each claim to an evidence ID.
3. Build the section outline.
4. Draft methods and results from approved artifacts.
5. Draft related work from verified original sources.
6. Draft introduction and abstract last so their claims match the paper.
7. Run citation, number, table, and terminology checks.
8. Prepare the G5 packet.

## Claim language

- Use `Prior work found...` for another scholar's result.
- Use `Our experiment shows...` only for approved `own_experiment` evidence.
- Use calibrated language such as `suggests`, `is consistent with`, or `does not establish` when uncertainty requires it.
- Avoid novelty superlatives such as `first` or `only` unless a documented search supports the bounded statement.

## BibTeX rules

- Create entries from the publisher, DOI registry, proceedings, official preprint page, or official dataset record.
- Preserve the correct publication status and version.
- Do not edit titles to fit manuscript claims.
- Keep stable citation keys and deduplicate DOI/arXiv identifiers.
- Exclude the bibliography from language-model rewriting.

## Numerical consistency

- Generate tables from approved analysis outputs when possible.
- Trace every headline number to a run and metric definition.
- Check rounding, denominators, averaging method, units, and confidence intervals.
- Treat conflicting numbers as blockers, not editorial choices.

## AI-use log

Record date, tool/model, purpose, input class, output used, human verification, and affected section. Never store secrets or confidential source text in the public repository.

## Final integrity review

- Confirm authors accept responsibility for all content.
- Confirm the target venue and institution's current AI, authorship, citation, and disclosure rules.
- Run similarity checking as a diagnostic, then manually inspect meaningful matches.
- Confirm no confidential reviewer material or third-party unpublished content was exposed to an external model.

