import matplotlib.pyplot as plt
import numpy as np

# Categories and dataset labels
categories = ['Original', 'Synonym Subst.', 'Typo', 'Rewording', 'Code-Switch']
variant_labels = ['MultiQ-SK', 'MultiQ-PL', 'SKQuAD', 'PoQuAD']
bar_width = 0.18
x = np.arange(len(categories))
colors = plt.get_cmap('tab10').colors

# Datasets
MultiQ_SK = np.array([
    [94, 52, 98],
    [90, 56, 98],
    [92, 42, 100],
    [92, 54, 100],
    [90, 50, 78]
])
MultiQ_PL = np.array([
    [90, 44, 100],
    [94, 38, 100],
    [84, 44, 98],
    [82, 38, 98],
    [88, 44, 78]
])
SKQuAD = np.array([
    [92, 18, 98],
    [90, 8, 98],
    [90, 18, 98],
    [88, 12, 96],
    [84, 10, 92]
])
PoQuAD = np.array([
    [70, 6, 100],
    [72, 8, 100],
    [78, 8, 100],
    [78, 6, 100],
    [60, 8, 92]
])

# Organize data by metric
grammatical = np.column_stack([MultiQ_SK[:, 0], MultiQ_PL[:, 0], SKQuAD[:, 0], PoQuAD[:, 0]])
factual = np.column_stack([MultiQ_SK[:, 1], MultiQ_PL[:, 1], SKQuAD[:, 1], PoQuAD[:, 1]])
language = np.column_stack([MultiQ_SK[:, 2], MultiQ_PL[:, 2], SKQuAD[:, 2], PoQuAD[:, 2]])
all_data = [grammatical, factual, language]
titles = ['Grammatical Correctness', 'Factual Correctness', 'Language Fidelity']

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(20, 6), sharey=True)

for idx, (ax, data, title) in enumerate(zip(axes, all_data, titles)):
    for j in range(len(variant_labels)):
        bars = ax.bar(x + j * bar_width, data[:, j], width=bar_width,
                      label=variant_labels[j], color=colors[j])
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.0f}',
                    ha='center', va='bottom', fontsize=8)

    ax.set_title(title, fontsize=14, weight='bold')
    ax.set_xticks(x + bar_width * 1.5)
    ax.set_xticklabels(categories, rotation=15)
    ax.set_ylabel('Percentage')
    ax.set_ylim(0, 110)
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Legend placement: left and right plots only
    if idx == 0 or idx == 2:
        ax.legend(loc='lower right', fontsize=9)

plt.tight_layout()
plt.show()
