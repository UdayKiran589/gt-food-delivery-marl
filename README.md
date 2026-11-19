# GT Food Delivery: Multi-Agent Reinforcement Learning

**GitHub repository:** https://github.com/UdayKiran589/gt-food-delivery-marl

A research-oriented project exploring multi-agent reinforcement learning
for food-delivery decisions, risk-sensitive control, LLM/RAG-guided
policies, and explainability.

## Paper

**Risk-Aware Multi-Agent Decision-Making for Competitive Food Delivery
Platforms: Integrating MAPPO, Distributional Reinforcement Learning,
Adaptive Risk, LLM/RAG Guidance, and Explainable AI** (IEEE conference format)

Authors: Uday Kiran, Santhosh, Rathan, Samhitha, and Dr. Nitesh Funde,
Department of Artificial Intelligence, SVNIT Surat, India

| File | Contents |
|---|---|
| `paper/main.tex` | Full manuscript: Introduction, Related Work, Datasets, Models 1–5, Integrated System, Findings, Conclusion, 25 references |
| `paper/main_short.tex` | Condensed version of the same paper (about 3,400 words) |
| `paper/figures/` | Result figures (PDF and PNG) |
| `paper/make_figures.py` | Script that regenerates the figures from archived results |

To build on Overleaf, upload a zip containing `main.tex` and the
`figures/` folder (New Project → Upload Project). It compiles with
pdfLaTeX or XeLaTeX. To rebuild the figures locally, run
`python paper/make_figures.py` (requires matplotlib and numpy).

```bash
git clone https://github.com/UdayKiran589/gt-food-delivery-marl.git
cd gt-food-delivery-marl
```

## Dataset and model resources

The agents train on trajectories from a custom two-platform market
simulator. The public datasets below are used only to calibrate the
simulator (demand patterns, delivery times, costs, restaurant prices);
agents never learn directly from the raw records.

| Resource | Used for | Link |
|---|---|---|
| Delivery Center: Food & Goods Orders in Brazil | Hourly order demand, delivery-cycle times, hub activity, delivery costs | https://www.kaggle.com/datasets/nosbielcs/brazilian-delivery-center |
| Zomato Bangalore Restaurants | Restaurant price levels, popularity, online-ordering behaviour | https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants |
| FLAN-T5-Small (Google) | Language-model action prior in Models 4 and 5 | https://huggingface.co/google/flan-t5-small |

The notebooks download both datasets automatically with `kagglehub`:

```python
import kagglehub
dc_dir  = kagglehub.dataset_download("nosbielcs/brazilian-delivery-center")
zom_dir = kagglehub.dataset_download("himanshupoddar/zomato-bangalore-restaurants")
```

FLAN-T5-Small is loaded through Hugging Face `transformers`
(`AutoModelForSeq2SeqLM` / `AutoTokenizer`). The model ID can be overridden
with the `FDM_M4_LLM_ID` environment variable. On Kaggle, the Model 5
notebook can instead use the attached model input
(`Input → Add Input → Models → google/flan-t5`).

## Implementation environment and setup

### Original environment

All experiments were developed and run in **Kaggle notebooks** (Python 3,
PyTorch with CUDA GPU acceleration). The notebooks read inputs from
`/kaggle/input/...` and write outputs to `/kaggle/working/`. One Model 2
notebook also contains an optional Google Colab download helper
(`google.colab.files`).

### Python packages used

| Purpose | Packages |
|---|---|
| Deep learning / RL | `torch` |
| Language model | `transformers` (FLAN-T5-Small) |
| Data handling | `numpy`, `pandas`, `scikit-learn` |
| Dataset download | `kagglehub` |
| Plotting and notebook UI | `matplotlib`, `ipywidgets`, `IPython` |

These are taken from the notebooks' imports. Exact versions have not
yet been pinned (see `documentation/ENVIRONMENT_NOTES.md`).

### Option A: Run on Kaggle (recommended)

1. Create a new Kaggle notebook and upload the notebook you want from
   `source/` (for example `source/model4/GT_Model4_ADAPTIVE_LLM_RAG_CHECKPOINTED.ipynb`).
2. Under **Settings**, turn on **Internet** (for `kagglehub` and Hugging Face downloads) and choose a **GPU** accelerator.
3. For Models 3–5, attach the required upstream checkpoint as a Kaggle
   dataset or model input (see the cautions under *Research integrity* below).
4. Run all cells.

### Option B: Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      Linux/macOS: source .venv/bin/activate
pip install torch transformers numpy pandas scikit-learn matplotlib kagglehub ipywidgets jupyter
jupyter notebook
```

- Install the CUDA build of PyTorch from https://pytorch.org if you have an NVIDIA GPU. CPU also runs but is slow.
- `kagglehub` needs Kaggle API credentials (`~/.kaggle/kaggle.json`, or the `KAGGLE_USERNAME`/`KAGGLE_KEY` environment variables). Never commit these files.
- Replace the `/kaggle/input` and `/kaggle/working` paths in the notebook with local folders.

### Seeds and key settings

The main training seed is `700` (Models 3–5). The Model 5 normal and
genuine-shock evaluations use separate seeds that are defined in the
notebook. Evaluation episodes are 168 decision steps long. The genuine-shock
condition raises the demand-volatility parameter from 0.12 to 0.30.

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
