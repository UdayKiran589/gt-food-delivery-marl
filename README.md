# GT Food Delivery: Multi-Agent Reinforcement Learning

A research-oriented project exploring multi-agent reinforcement learning
for food-delivery decisions, risk-sensitive control, LLM/RAG-guided
policies, and explainability.

## Research components

| Model | Research focus | Repository status |
|---|---|---|
| Model 1 | MAPPO/PPO baseline | Baseline notebook included; rerun and environment verification pending |
| Model 2 | MAPPO, forecasting, and counterfactual-advantage experiments | Two research notebooks included; data and checkpoint dependencies remain |
| Model 3 | Risk-sensitive MAPPO and CVaR | Reported results exist in the archive; checkpoint lineage remains unresolved |
| Model 4 | Adaptive risk control, LLM/RAG prior, and uncertainty gating | Notebook included; requires a verified Model 3 checkpoint and environment setup |
| Model 5 | Feature sensitivity, faithfulness, and counterfactual explanations | Integrated research notebook copy included; upstream dependencies and evidence provenance require validation |

Notebook inclusion does not imply independent reproduction or validation.

## Repository structure

- `source/model1_baseline/` — Model 1 baseline notebook
- `source/model2_mappo/` — Model 2 training and repair/ablation notebooks
- `source/model4/` — Model 4 adaptive-control notebook
- `source/model5_integrated/` — cleaned publication copy of the integrated research notebook
- `documentation/` — model status, inventory, experiment log, reproducibility guide, and environment notes
- `results/` — selected results only after review and approval for publication

The original integrated notebook remains in the research archive. The
repository copy removes the exceptionally large saved download-button
output while retaining the notebook's code. Other saved outputs remain
and must be interpreted as archived notebook outputs, not proof of an
independently reproduced run.

## Reproduction status

The notebooks were developed with a Kaggle-style environment and use
Kaggle paths, datasets, and/or saved checkpoints. A clean clone is not
currently sufficient to reproduce every experiment.

Before attempting a reproduction:

1. Read `documentation/REPRODUCIBILITY.md`,
   `documentation/EXPERIMENT_LOG.md`, and
   `documentation/MODEL_STATUS.md`.
2. Inspect the notebook's required datasets, paths, checkpoints, and packages.
3. Verify checkpoint provenance and ensure that the required model is the
   correct initialization model.
4. Record environment, hardware, seeds, configuration, and observed metrics.
5. Preserve failed and negative results as well as positive results.

The archived environment freeze is not a verified minimal requirements
file. Installation instructions will be added after dependency review
and validation in a clean environment.

## Research integrity and limitations

- Model 3 checkpoint and baseline discrepancies remain unresolved.
- Notebook-reported results are not independently reproduced results.
- Model 4 requires a verified Model 3 checkpoint; do not silently substitute
  a Model 2 checkpoint.
- Counterfactual analyses that hold the recorded LLM prior and uncertainty
  gate fixed measure conditional sensitivity.
- Do not claim a model is superior without appropriate baselines,
  controlled comparisons, and supporting evaluation.

## Artifact and security policy

Model checkpoints, large archives, private credentials, API keys, private
data, and unreviewed outputs must not be committed by default. Review
notebook code and saved outputs before publication. Only load serialized
checkpoint files from trusted sources.

See `documentation/MODEL_INVENTORY.txt`,
`documentation/MODEL_STATUS.md`, and
`documentation/ENVIRONMENT_NOTES.md` for current limitations.
