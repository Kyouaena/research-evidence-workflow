# Method-specific controls

## LLM and Agent safety evaluation

- Define threat model, attacker knowledge, attack surface, protected action, and failure event.
- Separate attack generation, victim model, defense model, and judge when independence matters.
- Freeze attack payload development and held-out test sets.
- Record complete model identifiers, access dates, prompts, system messages, decoding parameters, tool schemas, retries, and refusal handling.
- Measure safety and utility together. Report attack success rate with task success, false positives, latency, and cost where relevant.
- Use repeated runs or resampling when model stochasticity affects estimates.
- Report confidence intervals and manually review a defined sample of disputed or positive cases.
- Prevent judge leakage and circular evaluation. Document whether the judge sees labels, defenses, or expected outputs.
- Treat provider model updates as a reproducibility limitation and record dates.

## Financial time-series forecasting

- Order every observation by the time information became available, not by a revised timestamp.
- Use chronological or rolling-origin splits. Never random-shuffle forecasting data across time.
- Fit preprocessing, feature selection, and hyperparameters only on training/development windows.
- Prevent look-ahead bias from revised macroeconomic data, publication delays, future text, and full-sample normalization.
- Compare against simple and domain-relevant baselines, including naive persistence where appropriate.
- Report forecast horizon, window design, update frequency, transaction assumptions, and missing-data treatment.
- Evaluate statistical and practical significance. Use time-series-aware uncertainty or forecast comparison tests when assumptions fit.
- Separate predictive accuracy from trading profitability and state whether costs and slippage are included.

## System prototypes

- Define the minimum testable architecture and interfaces before implementation.
- Trace each component to a research hypothesis or engineering necessity.
- Record dependency versions, configuration, API schemas, and failure recovery.
- Separate prototype demonstration from evidence of general effectiveness.
- Test deterministic components with unit tests and model-dependent components with frozen evaluation cases.

## Ablation studies

- Start from a reproducible full model and a clearly defined baseline.
- Remove or replace one factor at a time unless testing an explicitly modeled interaction.
- Hold data, prompts, seeds, model versions, and evaluation code constant.
- Predefine the primary comparison and uncertainty method.
- Report all planned ablations, including null or harmful effects.
- Do not infer component necessity solely from one stochastic run.
- Distinguish performance contribution, safety contribution, and cost contribution.

