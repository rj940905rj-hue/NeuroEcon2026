from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)


BLUE = "#2557A7"
RED = "#B64A36"
GOLD = "#C69235"
GRAY = "#D6DADF"
GRID = "#E8EBEF"


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.edgecolor": "#4A4A4A",
        "axes.linewidth": 0.8,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def finish(fig, ax, name, legend=False):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y")
    if legend:
        ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"{name}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def add_bar_labels(ax, bars, fmt="{:.0f}", dy=0.02):
    ymax = ax.get_ylim()[1]
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + ymax * dy,
            fmt.format(h),
            ha="center",
            va="bottom",
            fontsize=10,
        )


def cell_counts():
    labels = ["Glutamatergic", "GABAergic"]
    vals = [9006, 3331]
    fig, ax = plt.subplots(figsize=(4.3, 3.7))
    bars = ax.bar(labels, vals, color=[BLUE, RED], width=0.6)
    ax.set_title("Cell counts")
    ax.set_ylabel("Recorded neurons")
    ax.set_ylim(0, 10000)
    add_bar_labels(ax, bars)
    finish(fig, ax, "cell_counts")


def social_responsiveness():
    labels = ["Glutamatergic", "GABAergic"]
    vals = [10, 45]
    fig, ax = plt.subplots(figsize=(4.3, 3.7))
    bars = ax.bar(labels, vals, color=[BLUE, RED], width=0.6)
    ax.set_title("Social responsiveness")
    ax.set_ylabel("Social-responsive neurons (%)")
    ax.set_ylim(0, 50)
    add_bar_labels(ax, bars)
    finish(fig, ax, "social_responsiveness")


def decoding_summary():
    labels = ["Attack-\nSniff", "Attack-\nApproach", "Attack-\nSelf groom", "Sniff-\nSelf groom"]
    gaba = np.array([0.92, 0.83, 0.73, 0.89])
    glut = np.array([0.62, 0.58, 0.55, 0.68])
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    b1 = ax.bar(x - w / 2, gaba, width=w, color=RED, label="GABAergic")
    b2 = ax.bar(x + w / 2, glut, width=w, color=BLUE, label="Glutamatergic")
    ax.set_title("Social behavior decoding")
    ax.set_ylabel("Balanced accuracy")
    ax.set_xticks(x, labels)
    ax.set_ylim(0.45, 1.0)
    add_bar_labels(ax, b1, fmt="{:.2f}", dy=0.015)
    add_bar_labels(ax, b2, fmt="{:.2f}", dy=0.015)
    finish(fig, ax, "decoding_summary", legend=True)


def shared_unique_variance():
    labels = ["Glutamatergic", "GABAergic"]
    shared = np.array([5, 30])
    unique = np.array([95, 70])
    fig, ax = plt.subplots(figsize=(4.5, 3.9))
    b1 = ax.bar(labels, shared, color=GOLD, width=0.6, label="Shared")
    b2 = ax.bar(labels, unique, bottom=shared, color=GRAY, width=0.6, label="Unique")
    ax.set_title("Shared vs unique variance")
    ax.set_ylabel("Neural variance (%)")
    ax.set_ylim(0, 100)
    add_bar_labels(ax, b1)
    for bar, base in zip(b2, shared):
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            base + h / 2,
            f"{int(h)}",
            ha="center",
            va="center",
            fontsize=10,
            color="#3E3E3E",
        )
    finish(fig, ax, "shared_unique_variance", legend=True)


def top_dimension():
    labels = ["Glutamatergic", "GABAergic"]
    vals = [1.0, 3.5]
    fig, ax = plt.subplots(figsize=(4.3, 3.7))
    bars = ax.bar(labels, vals, color=[BLUE, RED], width=0.6)
    ax.set_title("Top shared dimension (PLSC1)")
    ax.set_ylabel("Relative variance explained")
    ax.set_ylim(0, 4.0)
    add_bar_labels(ax, bars, fmt="{:.1f}")
    finish(fig, ax, "top_dimension")


def mutual_interaction_trend():
    x = np.array([12, 18, 22, 28, 35, 42, 55, 61, 68, 72, 78, 85, 90, 95])
    y = np.array([8, 10, 12, 11, 15, 16, 18, 22, 21, 24, 27, 28, 30, 31])
    fig, ax = plt.subplots(figsize=(5.0, 3.8))
    ax.scatter(x, y, s=42, color=RED, zorder=3)
    coeffs = np.polyfit(x, y, 1)
    xx = np.linspace(10, 96, 200)
    ax.plot(xx, coeffs[0] * xx + coeffs[1], color=BLUE, linewidth=2.2)
    ax.set_title("More mutual interaction, more shared subspace")
    ax.set_xlabel("Mutual social interaction level")
    ax.set_ylabel("Shared variance (%)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 35)
    finish(fig, ax, "mutual_interaction_trend")


def coordinated_vs_uncoordinated():
    labels = ["Full behavior", "Aggressive moments"]
    coordinated = np.array([9, 20])
    uncoordinated = np.array([91, 80])
    fig, ax = plt.subplots(figsize=(4.8, 3.9))
    b1 = ax.bar(labels, coordinated, color=GOLD, width=0.6, label="Coordinated")
    b2 = ax.bar(labels, uncoordinated, bottom=coordinated, color=GRAY, width=0.6, label="Uncoordinated")
    ax.set_title("Coordinated vs uncoordinated")
    ax.set_ylabel("Behavioral variance (%)")
    ax.set_ylim(0, 100)
    add_bar_labels(ax, b1)
    for bar, base in zip(b2, coordinated):
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            base + h / 2,
            f"{int(h)}",
            ha="center",
            va="center",
            fontsize=10,
            color="#3E3E3E",
        )
    finish(fig, ax, "coordinated_vs_uncoordinated", legend=True)


def ai_emergence():
    x = np.array([0, 4000, 8000, 12000, 16000, 20000])
    social = np.array([5, 18, 36, 55, 72, 82])
    nonsocial = np.array([5, 7, 8, 9, 11, 12])
    fig, ax = plt.subplots(figsize=(5.0, 3.8))
    ax.plot(x, social, color=RED, linewidth=2.6, marker="o", label="Social agents")
    ax.plot(x, nonsocial, color=BLUE, linewidth=2.3, linestyle="--", marker="o", label="Non-social agents")
    ax.set_title("Emergence of social interaction")
    ax.set_xlabel("Training iteration")
    ax.set_ylabel("Social behavior index")
    ax.set_xlim(0, 20000)
    ax.set_ylim(0, 100)
    finish(fig, ax, "ai_emergence", legend=True)


def ai_shared_dimensions():
    labels = ["Social", "Non-social", "Non-social\n+ vision"]
    vals = [7, 1, 1]
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    bars = ax.bar(labels, vals, color=[RED, BLUE, GRAY], width=0.6)
    ax.set_title("Shared dimensions in agents")
    ax.set_ylabel("Shared dimensions")
    ax.set_ylim(0, 10)
    add_bar_labels(ax, bars)
    finish(fig, ax, "ai_shared_dimensions")


def ai_decoding():
    labels = ["Collision", "Partner\napproach", "Partner\nescape"]
    social = np.array([0.86, 0.79, 0.82])
    nonsocial = np.array([0.53, 0.51, 0.52])
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    b1 = ax.bar(x - w / 2, social, width=w, color=RED, label="Social")
    b2 = ax.bar(x + w / 2, nonsocial, width=w, color=BLUE, label="Non-social")
    ax.set_title("Decoding partner-related events")
    ax.set_ylabel("Balanced accuracy")
    ax.set_xticks(x, labels)
    ax.set_ylim(0.45, 1.0)
    add_bar_labels(ax, b1, fmt="{:.2f}", dy=0.015)
    add_bar_labels(ax, b2, fmt="{:.2f}", dy=0.015)
    finish(fig, ax, "ai_decoding", legend=True)


def ai_perturbation():
    labels = ["Original", "Random PCs", "Shared PLSCs"]
    vals = [16, 15, 7]
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    bars = ax.bar(labels, vals, color=[RED, BLUE, GOLD], width=0.6)
    ax.set_title("Perturbation test")
    ax.set_ylabel("Collision time (%)")
    ax.set_ylim(0, 20)
    add_bar_labels(ax, bars)
    finish(fig, ax, "ai_perturbation")


def main():
    cell_counts()
    social_responsiveness()
    decoding_summary()
    shared_unique_variance()
    top_dimension()
    mutual_interaction_trend()
    coordinated_vs_uncoordinated()
    ai_emergence()
    ai_shared_dimensions()
    ai_decoding()
    ai_perturbation()


if __name__ == "__main__":
    main()
