# Reproducibility Guide

## Current scope

The repository preserves research notebooks and documents the known
implementation stages. A clean clone alone does not guarantee that every
experiment can be rerun: original notebook environments, datasets,
checkpoints, external services, and runtime settings may be required.

## Before running an experiment

1. Read `README.md`, `MODEL_STATUS.md`, and `EXPERIMENT_LOG.md`.
2. Inspect the selected notebook from top to bottom.
3. Identify its input data, artifact paths, environment variables,
   external services, and expected checkpoints.
4. Verify the provenance of each required checkpoint.
5. Record package versions, runtime/hardware, random seeds, and configuration.
6. Preserve the original notebook; conduct modifications in a separate copy
   or a tracked source file.

## Evaluation discipline

- Run control and intervention arms under comparable conditions.
- Record the actual output metrics and gate decisions.
- Report failed gates and negative results alongside positive results.
- Do not compare results from incompatible seeds, environments, or datasets
  as if they were controlled comparisons.
- Distinguish notebook-reported historical results from newly reproduced
  results.

## Model-specific cautions

- Model 2: retain the control-versus-counterfactual comparison and the
  measured final-arm selection rule.
- Model 3: do not claim validation until the checkpoint lineage is resolved.
- Model 4: verify the required Model 3 checkpoint before execution.
- Model 5: document which upstream quantities remain fixed in each
  counterfactual or faithfulness experiment.

## Checkpoints and data

Large checkpoints, private credentials, and sensitive data should not be
committed to the public repository by default. Record artifact provenance
and provide an appropriate reproducible acquisition or generation procedure
where possible.
