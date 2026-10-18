"""Rebuild README figures from committed results; requires matplotlib."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "research"
SEEDS = (42, 43, 44)
COLORS = ("#64748b", "#2563eb", "#d97706", "#059669")
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white"})

def read(seed, name):
    return json.loads((ROOT / f"reports/robustness/seed-{seed}/{name}.json").read_text())

def panel(ax, experiment, models, labels, metric, ylabel, limit):
    x = np.arange(3)
    width = .78 / len(models)
    for i, (model, label) in enumerate(zip(models, labels)):
        values = [read(s, experiment)["models"][model]["summary"][metric] for s in SEEDS]
        bars = ax.bar(x + (i - (len(models)-1)/2)*width, values, width,
                      label=label, color=COLORS[i])
        ax.bar_label(bars, fmt="%.2f", fontsize=8, padding=3)
    ax.set_xticks(x, [f"Seed {s}" for s in SEEDS])
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, limit)
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=.18)

def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=180, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 4.7))
panel(ax, "pathways", ["independent", "spatial", "pathway"],
      ["Independent", "Spatial", "Pathway"], "mean_error_mm", "Mean localization error (mm; lower is better)", 4.5)
ax.legend(loc="upper center", ncol=3, frameon=False)
ax.set_title("Plan A: no useful pathway advantage", loc="left", weight="bold", pad=15)
fig.text(.1, -.01, "Synthetic contacts | 120 test trials per seed | validation-selected smoothing | descriptive seed comparisons", fontsize=9)
save(fig, "pathway-results")

for experiment, models, labels, title, name in [
    ("receivers", ["raw", "fixed", "adaptive"], ["Raw", "Fixed", "Adaptive"],
     "Plan B: adaptive detection gains vary across seeds", "receiver-results"),
    ("combined", ["spatial_fixed", "spatial_adaptive", "pathway_fixed", "pathway_adaptive"],
     ["Spatial + fixed", "Spatial + adaptive", "Pathway + fixed", "Pathway + adaptive"],
     "Combined: compare detection and false alarms together", "combined-results")]:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    panel(axes[0], experiment, models, labels, "recall", "Event recall (higher is better)", 1.05)
    panel(axes[1], experiment, models, labels, "false_alarms_per_minute", "False alarms/min (lower is better)", 13 if experiment == "receivers" else 5.5)
    axes[1].axhline(3, color="#b91c1c", linestyle="--", linewidth=1.4)
    axes[1].text(.02, .94, "Dashed line: validation budget = 3/min", color="#b91c1c", transform=axes[1].transAxes, fontsize=9)
    fig.suptitle(title, x=.07, ha="left", weight="bold")
    handles, names = axes[0].get_legend_handles_labels()
    fig.legend(handles, names, loc="lower center", ncol=len(models), frameon=False, bbox_to_anchor=(.5, .02))
    fig.text(.07, -.015, "Synthetic held-out events | each threshold calibrated on validation | no physical-device or significance claim", fontsize=9)
    fig.subplots_adjust(bottom=.2, top=.87, wspace=.25)
    save(fig, name)
