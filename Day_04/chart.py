"""Render the sprint burndown from the checked CSV."""
import csv
from pathlib import Path
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
with (root / 'wallet_burndown.csv').open(newline='') as stream:
    records = [{key: int(value) for key, value in row.items()} for row in csv.DictReader(stream)]
days = [row['day'] for row in records]
remaining = [row['remaining_points'] for row in records]
assert days == list(range(11))
assert remaining[-1] == 0
for before, after in zip(records, records[1:]):
    assert after['remaining_points'] == before['remaining_points'] + after['scope_change'] - after['completed_points']
fig, ax = plt.subplots(figsize=(8.8, 5.0), layout='constrained')
ax.plot(days, [remaining[0] * (10-day)/10 for day in days], '--', color='#62748a', label='Ideal pace')
ax.plot(days, remaining, 'o-', color='#006b62', linewidth=2.5, markersize=5, label='Simulation')
ax.annotate('Day 4 · refund scope swap', xy=(4, 18), xytext=(4.35, 21.5),
            arrowprops={'arrowstyle': '->', 'color': '#27364a'}, color='#27364a')
ax.set(title='Digital wallet sprint burndown', xlabel='Sprint day', ylabel='Story points remaining',
       xticks=days, ylim=(0, 25))
ax.grid(axis='y', alpha=0.25)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper right', frameon=False)
fig.savefig(root / 'wallet_burndown.png', dpi=180)
