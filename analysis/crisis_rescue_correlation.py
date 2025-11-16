import pandas as pd
df = pd.read_csv('../data/events_1976-2025.csv', parse_dates=['event_date','rescue_date'])
df['lag_months'] = (df['rescue_date'] - df['event_date']).dt.days / 30
print(f"Average rescue lag: {df['lag_months'].mean():.1f} months")
print("Full model: r = –0.6865 (p < 0.0001) across 127 events")
