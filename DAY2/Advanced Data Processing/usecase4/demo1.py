import pandas as pd

# Load
df = pd.read_csv("cdr_raw.csv")

# Transform
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['duration_min'] = df['duration_sec'] / 60

# Aggregate
usage = df.groupby('caller').agg(
    total_calls=('caller', 'count'),
    total_duration=('duration_min', 'sum')
).reset_index()

# Save
usage.to_csv("cdr_summary.csv", index=False)

print("CDR Processing Done")
