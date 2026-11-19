"""Generate the five result figures for the IEEE paper.

All values are copied from:
  - GT.EXPLAIN.pdf (Tables 3-7)
  - results/model4/model4_normal_shock_evaluation.csv
  - results/model5/model5_normal_vs_genuine_shock_influence.csv
  - archived outputs of source/model5_integrated/GT_Project_Full_Model5_GitHub.ipynb
    (cell 141: shock volatility validation; cell 147: faithfulness;
     cells 148-149: counterfactual statistics)
No value is estimated or interpolated.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

BLUE, ORANGE = "#0072B2", "#E69F00"      # normal, genuine shock
GREY, GREEN = "#8C8C8C", "#009E73"       # adaptive control, full Model 4
INK, MUTED = "#1A1A1A", "#555555"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 8,
    "axes.titlesize": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7,
    "legend.fontsize": 7.5,
    "axes.edgecolor": MUTED,
    "axes.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": "#E3E3E3",
    "grid.linewidth": 0.5,
    "axes.axisbelow": True,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "xtick.major.size": 0,
    "ytick.major.width": 0.5,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})

COL_W = 3.5     # IEEE single column width (in)
PAGE_W = 7.16   # IEEE two-column text width (in)


def label_bars(ax, bars, fmt, pad_frac=0.015, size=6.5):
    top = ax.get_ylim()[1]
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, h + top * pad_frac, fmt(h),
                ha="center", va="bottom", fontsize=size, color=INK)


def grouped(ax, groups, series, colors, names, width=0.36, gap=0.02):
    x = np.arange(len(groups))
    n = len(series)
    offs = (np.arange(n) - (n - 1) / 2) * (width + gap)
    bars = []
    for vals, c, nm, o in zip(series, colors, names, offs):
        bars.append(ax.bar(x + o, vals, width, color=c, label=nm,
                           edgecolor="white", linewidth=0.6))
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    return bars


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=600)
    plt.close(fig)


# ---------------------------------------------------------------- Figure A
# Model 4 performance comparison (PDF Tables 4 and 5).
def fig_model4_performance():
    conds = ["Normal", "Genuine shock"]
    adaptive = {"profit": [344.8984, 314.2400],
                "fulfil": [0.8504, 0.8124],
                "cvar": [4.8128, 5.3776]}
    full = {"profit": [356.0009, 328.2573],
            "fulfil": [0.8775, 0.8424],
            "cvar": [4.2483, 4.8655]}
    panels = [("profit", "(a) Profit per hour", "Profit per hour", (0, 400),
               lambda v: f"{v:.1f}"),
              ("fulfil", "(b) Fulfilment rate", "Fulfilment rate", (0, 1.0),
               lambda v: f"{v:.4f}"),
              ("cvar", "(c) Tail CVaR (lower is better)", "Tail CVaR",
               (0, 6.2), lambda v: f"{v:.4f}")]
    fig, axes = plt.subplots(1, 3, figsize=(PAGE_W, 2.05))
    for ax, (k, title, ylab, ylim, fmt) in zip(axes, panels):
        ax.set_ylim(*ylim)
        bars = grouped(ax, conds, [adaptive[k], full[k]], [GREY, GREEN],
                       ["Adaptive control", "Full Model 4"])
        for b in bars:
            label_bars(ax, b, fmt, size=6.2)
        ax.set_title(title, loc="left", color=INK)
        ax.set_ylabel(ylab)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, 1.07))
    fig.tight_layout(w_pad=1.6)
    save(fig, "fig_model4_performance")


# ---------------------------------------------------------------- Figure B
# Shock volatility validation (notebook cell 141, 672 steps per condition).
def fig_shock_validation():
    metrics = ["Noise std.\ndeviation", "Mean absolute\nnoise",
               "95th percentile\nabsolute noise"]
    normal = [0.119315, 0.095966, 0.234386]
    shock = [0.293960, 0.236492, 0.568516]
    fig, ax = plt.subplots(figsize=(COL_W, 2.1))
    ax.set_ylim(0, 0.66)
    bars = grouped(ax, metrics, [normal, shock], [BLUE, ORANGE],
                   ["Normal", "Genuine shock"])
    for b in bars:
        label_bars(ax, b, lambda v: f"{v:.4f}", size=6.3)
    ax.set_ylabel("Normalised demand noise")
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save(fig, "fig_shock_validation")


# ---------------------------------------------------------------- Figure C
# Adaptive risk estimator (PDF Table 3; std from results/model5 CSV).
def fig_risk_estimator():
    conds = ["Normal", "Genuine shock"]
    mean = [0.4072, 0.7019]
    std = [0.0608, 0.1208]
    fig, ax = plt.subplots(figsize=(COL_W, 2.0))
    x = np.arange(2)
    ax.bar(x, mean, 0.5, color=[BLUE, ORANGE], edgecolor="white",
           linewidth=0.6)
    ax.errorbar(x, mean, yerr=std, fmt="none", ecolor=INK, elinewidth=0.8,
                capsize=4, capthick=0.8)
    for xi, m, s in zip(x, mean, std):
        ax.text(xi + 0.27, m, f"{m:.4f}\n$\\pm${s:.4f}", va="center",
                ha="left", fontsize=6.8, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels(conds)
    ax.set_xlim(-0.5, 1.95)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Mean estimated risk score $r_t$")
    fig.tight_layout()
    save(fig, "fig_risk_estimator")


# ---------------------------------------------------------------- Figure D
# Explanation faithfulness (notebook cell 147, 256 samples per group).
def fig_faithfulness():
    groups = ["Top-ranked", "Bottom-ranked"]
    flip = {"normal": [0.230469, 0.031250], "shock": [0.242188, 0.027344]}
    margin = {"normal": [1.407382, 0.069221], "shock": [1.455413, 0.068609]}
    fig, axes = plt.subplots(1, 2, figsize=(COL_W, 2.15))
    specs = [(axes[0], flip, "(a) Action-flip rate", "Action-flip rate",
              (0, 0.30), lambda v: f"{v:.3f}"),
             (axes[1], margin, "(b) Margin change",
              "Mean abs. margin change", (0, 1.75), lambda v: f"{v:.3f}")]
    for ax, d, title, ylab, ylim, fmt in specs:
        ax.set_ylim(*ylim)
        bars = grouped(ax, groups, [d["normal"], d["shock"]], [BLUE, ORANGE],
                       ["Normal", "Genuine shock"], width=0.38)
        for b in bars:
            label_bars(ax, b, fmt, size=5.6)
        ax.set_title(title, loc="left", color=INK)
        ax.set_ylabel(ylab)
        ax.tick_params(axis="x", labelsize=6.8)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, 1.08))
    fig.tight_layout(w_pad=1.2)
    save(fig, "fig_faithfulness")


# ---------------------------------------------------------------- Figure E
# (a) LLM influence (PDF Table 6; KL and logit change from results/model5 CSV)
# (b) Counterfactual analysis (PDF Table 7; notebook cells 148-149).
def fig_llm_counterfactual():
    panels_a = [("Mean confidence gate", [0.1340, 0.1322], "{:.4f}", 0.17),
                ("Action-change rate (%)", [1.54, 1.84], "{:.2f}", 2.3),
                (r"Mean KL (full $\|$ RL) $\times 10^{4}$", [1.906, 1.785],
                 "{:.3f}", 2.4),
                ("Mean abs. logit change", [0.5085, 0.5000], "{:.4f}", 0.65)]
    panels_b = [("Decision coverage (%)", [36.33, 35.94], "{:.2f}", 45),
                ("Feature-level flip rate (%)", [10.13, 10.16], "{:.2f}", 13),
                ("Successful counterfactuals", [363, 364], "{:d}", 460)]
    fig = plt.figure(figsize=(PAGE_W, 3.55))
    gs = fig.add_gridspec(2, 12, hspace=0.95, wspace=4.2)
    axes_a = [fig.add_subplot(gs[0, 3 * i:3 * i + 3]) for i in range(4)]
    axes_b = [fig.add_subplot(gs[1, 4 * i:4 * i + 4]) for i in range(3)]
    x = np.arange(2)
    for ax, (title, vals, fmt, top) in zip(axes_a + axes_b,
                                            panels_a + panels_b):
        bars = ax.bar(x, vals, 0.6, color=[BLUE, ORANGE], edgecolor="white",
                      linewidth=0.6)
        ax.set_ylim(0, top)
        label_bars(ax, bars, lambda v, f=fmt: f.format(v), size=6.5)
        ax.set_xticks(x)
        ax.set_xticklabels(["Normal", "Shock"])
        ax.set_title(title, color=INK, fontsize=7.3)
    fig.text(0.005, 0.985, "(a) LLM influence", fontsize=8.5,
             fontweight="bold", color=INK, va="top")
    fig.text(0.005, 0.47, "(b) Counterfactual analysis", fontsize=8.5,
             fontweight="bold", color=INK, va="top")
    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(color=BLUE, label="Normal"),
                        Patch(color=ORANGE, label="Genuine shock")],
               loc="upper right", ncol=2, frameon=False,
               bbox_to_anchor=(1.0, 1.02))
    save(fig, "fig_llm_counterfactual")


if __name__ == "__main__":
    fig_model4_performance()
    fig_shock_validation()
    fig_risk_estimator()
    fig_faithfulness()
    fig_llm_counterfactual()
    print("figures written to", OUT)
