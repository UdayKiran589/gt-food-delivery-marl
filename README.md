# GT Food Delivery: Multi-Agent Reinforcement Learning

A research-oriented project exploring multi-agent reinforcement learning
for food-delivery market and environment decisions, with risk-sensitive
control, LLM/RAG-guided policies, and explainability analysis.

## Research components

| Model | Research focus | Current status |
|---|---|---|
| Model 2 | MAPPO and counterfactual-advantage experiments | Archived experiments available; results require context |
| Model 3 | Risk-sensitive MAPPO and CVaR | Reported training results exist; checkpoint discrepancy unresolved |
| Model 4 | Adaptive risk control, LLM/RAG prior, uncertainty gating | Notebook included; reproduction dependencies remain to be resolved |
| Model 5 | Feature sensitivity, faithfulness, counterfactual explanations | Evidence files exist in the research archive; further validation is needed |

## Repository structure

- `source/model4/` — Model 4 research notebook
- `documentation/` — model status, inventory, and environment notes
- `results/` — selected research results, when reviewed and approved for publication

## Running the notebook

The Model 4 notebook was developed for a Kaggle-style environment and
currently references Kaggle input/output paths. It expects a compatible
Model 3 final checkpoint. Resolve that dependency and review the
environment and data requirements before attempting reproduction.

The archived environment freeze is not a verified minimal requirements
file. Installation instructions will be added after the dependencies
have been validated.

## Research integrity and limitations

- Model 3 checkpoint and baseline discrepancies remain unresolved.
- Notebook-reported results should not be treated as independently reproduced.
- Counterfactual analyses that hold the recorded LLM prior and uncertainty
  gate fixed measure conditional sensitivity.
- Negative, mixed, and failed experiments should be reported honestly.
- Do not claim a model is superior without supporting evaluation and
  appropriate comparisons.

## Artifact and security policy

Model checkpoints and large binary artifacts are excluded from this
repository by default. Do not commit credentials, API keys, private data,
or unreviewed outputs.

See `documentation/MODEL_STATUS.md` and
`documentation/ENVIRONMENT_NOTES.md` for current limitations.
