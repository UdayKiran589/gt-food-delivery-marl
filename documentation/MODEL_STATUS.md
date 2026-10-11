# Model Status and Research Notes

## Model 2 — MAPPO
MAPPO and counterfactual-advantage experiments are present in the
research archive. Training checkpoints and binary model artifacts
are excluded from this public repository.

## Model 3 — Risk-Sensitive MAPPO
Notebook logs report distributional quantile-critic training and
CVaR-based risk evaluation. The final Model 3 checkpoint and its
relationship to the initialization artifact still require verification.
Do not treat Model 3 results as independently reproduced.

## Model 4 — Adaptive Control
The Model 4 notebook is included under `source/model4/`.
It combines adaptive risk control, an LLM/RAG policy prior,
uncertainty gating, MAPPO training, evaluation, and ablations.

The notebook currently uses Kaggle-specific input/output paths.
A compatible Model 3 final checkpoint is required by its initialization
logic. Reproduction requires resolving that dependency and reviewing
the required dataset, environment, and package setup.

## Model 5 — Explainability
The research archive contains feature-sensitivity, faithfulness,
and counterfactual-analysis evidence for the integrated Model 4 policy.

The documented counterfactual experiments hold the recorded LLM prior
and uncertainty gate fixed. Interpret them as conditional sensitivity
analyses, not as tests that regenerate those components.

## Outstanding validation
- Reconcile the Model 3 baseline/checkpoint discrepancy.
- Verify model initialization and dependency paths.
- Re-run experiments from documented inputs before claiming reproduction.
- Report negative or mixed results alongside positive results.
