import pandas as pd
import matplotlib.pyplot as plt

rescue = pd.read_csv('./data/events_1976-2025.csv', parse_dates=['rescue_date'])
donations = pd.read_csv('./data/fec_prc_donations_2016-2024.csv', parse_dates=['date'])

fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(rescue['rescue_date'], rescue['amount_usd']/1e6, 'o-', color='steelblue', label='Rescue (M USD)')
ax1.set_ylabel('Rescue Amount (M USD)', color='steelblue')

ax2 = ax1.twinx()
ax2.plot(donations['date'], donations['amount']/1e3, 's-', color='crimson', alpha=0.7, label='Donation (K USD)')
ax2.set_ylabel('Donation Amount (K USD)', color='crimson')

ax1.set_title('Stress → Resource Inflow: Two Signals, One Pattern\n'
              'No causal claim — timing only')
ax1.set_xlabel('Year')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.tight_layout()
plt.savefig('./viz/combined_timeline.png', dpi=300)
print("Fusion viz → viz/combined_timeline.png")
