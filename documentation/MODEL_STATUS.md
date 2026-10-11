# Model Status and Research Notes

## Model 1 — MAPPO/PPO baseline

The baseline notebook is included at
`source/model1_baseline/GT_Model1_MAPPO_Baseline.ipynb`.

The notebook references CSV datasets, including stores, orders, and
deliveries data. Verify dataset provenance and availability, environment
requirements, and a clean rerun before claiming reproduction.

## Model 2 — MAPPO and counterfactual advantages

Two notebooks are included under `source/model2_mappo/`: the main
checkpointed training notebook and the repair/counterfactual ablation
notebook.

They use dataset files, saved model artifacts, and checkpoint discovery
logic that includes Kaggle-specific paths. Verify artifact provenance,
the selected checkpoint, and the control-versus-counterfactual comparison
before interpreting results as reproduced.

## Model 3 — Risk-sensitive MAPPO

Notebook logs in the research archive report distributional quantile-critic
training and CVaR-based risk evaluation. The final Model 3 checkpoint and
its relationship to the initialization artifact still require verification.
Do not treat Model 3 results as independently reproduced.

A Model 3 source notebook is not currently included in this repository.

## Model 4 — Adaptive control

The Model 4 notebook is included under `source/model4/`. It combines
adaptive risk control, an LLM/RAG policy prior, uncertainty gating,
MAPPO training, evaluation, and ablations.

The notebook uses Kaggle-specific paths and requires a compatible,
verified Model 3 final checkpoint. Its checkpoint-discovery logic is
intended to reject silent substitution of a Model 2 counterfactual
checkpoint. Preserve this safeguard while resolving the dependency.

## Model 5 — Explainability / integrated notebook

The cleaned publication copy is included at
`source/model5_integrated/GT_Project_Full_Model5_GitHub.ipynb`.

It contains feature-sensitivity, faithfulness, and counterfactual-analysis
stages and references upstream Model 2 artifacts through Kaggle paths.
The original integrated notebook remains in the research archive.

The publication copy removes the exceptionally large saved output from
the download-button cell but retains the code and other saved outputs.
Inspect remaining outputs and verify evidence provenance before publication
claims. Counterfactual experiments that hold the recorded LLM prior and
uncertainty gate fixed measure conditional sensitivity, not a complete
regeneration of the upstream decision system.

## Outstanding validation

- Reconcile the Model 3 baseline/checkpoint discrepancy.
- Verify the provenance and intended role of each initialization artifact.
- Document dataset acquisition and checkpoint requirements.
- Validate package and runtime requirements in a clean environment.
- Re-run experiments from documented inputs before claiming reproduction.
- Report negative or mixed results alongside positive results.
