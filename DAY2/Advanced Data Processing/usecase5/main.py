import pandas as pd

# Load JSON
df = pd.read_json("network.json")

print("Raw Data:")
print(df)

# Data Transformation & Normalization
# Convert timestamp + normalize metrics
# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Normalize packet_loss → percentage
df['packet_loss_%'] = df['packet_loss'] * 100

# Normalize latency (optional scaling)
df['latency_ms'] = df['latency']

# Drop old column if needed
df = df.drop(columns=['packet_loss'])

print("\nTransformed Data:")
print(df)

# Filtering Data - Example: Identify bad network performance
# High latency or packet loss
alerts = df[(df['latency_ms'] > 40) | (df['packet_loss_%'] > 50)]

print("\nNetwork Alerts:")
print(alerts)

# Grouping & Summarization
summary = df.groupby('tower_id').agg(
    avg_latency=('latency_ms', 'mean'),
    max_latency=('latency_ms', 'max'),
    avg_packet_loss=('packet_loss_%', 'mean')
).reset_index()

print("\nTower Summary:")
print(summary)

# Convert Log Data → Structured Format
raw_logs = [
    "T1|2026-04-20 12:00|lat=30|loss=0.2",
    "T2|2026-04-20 12:00|lat=60|loss=0.7",
    "T3|2026-04-20 12:00|lat=20|loss=0.1"
]

log_data = []

for log in raw_logs:
    parts = log.split("|")
    record = {
        "tower_id": parts[0],
        "timestamp": parts[1],
        "latency": float(parts[2].split("=")[1]),
        "packet_loss": float(parts[3].split("=")[1])
    }
    log_data.append(record)

log_df = pd.DataFrame(log_data)

print("\nParsed Log Data:")
print(log_df)

# Save Clean Data
df.to_csv("clean_tower_data.csv", index=False)
summary.to_csv("tower_summary.csv", index=False)


report = {
    "total_records": len(df),
    "total_towers": df['tower_id'].nunique(),
    "avg_latency_overall": df['latency_ms'].mean(),
    "avg_packet_loss_overall": df['packet_loss_%'].mean(),
    "worst_tower": summary.sort_values('avg_latency', ascending=False).iloc[0]['tower_id']
}

print("\nEngineering Report:")
for k, v in report.items():
    print(f"{k}: {v}")
