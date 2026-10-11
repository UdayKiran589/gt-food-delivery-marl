# Experiment Log

This log records the research implementation history. Results are not
considered independently reproduced merely because a notebook contains
saved output or reports a successful gate.

## Model 1 — MAPPO Baseline

- Source: `gt_model.ipynb` in the research archive.
- Role: Baseline multi-agent policy and evaluation pipeline.
- Reported evaluation dimensions include profit, fulfillment, delay,
  tail CVaR, and fairness-related metrics.
- Status: Historical baseline; rerun and environment verification required.

## Model 2 — Forecasting and Counterfactual Advantages

- Primary source:
  `source/model2_mappo/gt_model_v2_predict_checkpointed.ipynb`
- Repair and comparison source:
  `source/model2_mappo/GT_Model2_Repair_and_Counterfactual_Ablations.ipynb`
- Methods include demand forecasting, a residual world model, and
  counterfactual rollouts for action comparison and policy training.
- The repair notebook compares control and counterfactual arms and
  selects the final arm using recorded performance and gate conditions.
- Interpretation: counterfactual training is not assumed to be superior.
  The selected arm and its supporting metrics must be recorded from the
  actual experiment output.
- Status: Implementation archived; independent reproduction pending.

## Model 3 — Risk-Sensitive Policy

- Status: Unresolved.
- The provenance of the expected Model 3 initialization checkpoint has
  not been established.
- A checkpoint in the Model 4 archive was found to have the same SHA-256
  hash as a Model 2 final checkpoint.
- Do not report Model 3 as independently trained or validated until its
  source, training procedure, and checkpoint lineage are verified.

## Model 4 — Adaptive Risk and Control

- Source:
  `source/model4/GT_Model4_ADAPTIVE_LLM_RAG_CHECKPOINTED.ipynb`
- Includes adaptive risk control, LLM/RAG-related components, uncertainty
  gating, and evaluation/ablation logic.
- The notebook explicitly rejects silently substituting a Model 2
  checkpoint when a valid Model 3 checkpoint is required.
- Status: Source archived; execution and dependency verification pending.

## Model 5 — Explainability

- Source notebook in the research archive:
  `gt-project-full.ipynb`
- Identified stages include normal-versus-shock influence analysis,
  feature sensitivity, observation-semantic mapping, faithfulness tests,
  conditional policy counterfactuals, and final evidence aggregation.
- The documented counterfactual analysis holds some upstream quantities
  fixed. Its conclusions must therefore be described as conditional
  sensitivity, not as a full regeneration of the upstream decision system.
- Status: Source and archived evidence identified; independent reproduction
  and evidence-to-run provenance verification pending.

## Research Record Requirements

For each meaningful experiment, record:

1. Experiment ID and date.
2. Source notebook revision and configuration.
3. Dataset/environment and random seeds.
4. Baselines, controls, and intervention conditions.
5. Metrics, gate criteria, and actual observed results.
6. Checkpoint provenance, where applicable.
7. Limitations, failed tests, and unresolved discrepancies.

Never convert a notebook's printed PASS message into a claim of independent
validation without verifying the underlying run and its artifacts.
