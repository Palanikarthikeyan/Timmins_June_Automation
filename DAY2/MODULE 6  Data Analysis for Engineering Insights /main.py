import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("multi_day_kpi_logs.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date

print("Dataset Preview:")
print(df.head())

# ----------------------------------
# 1. Basic Statistical Analysis
# ----------------------------------
print("\nStatistical Summary:")
print(df.describe())

# ----------------------------------
# 2. Trend Analysis (Daily Averages)
# ----------------------------------
daily_trend = df.groupby('date').agg({
    'latency_ms': 'mean',
    'packet_loss': 'mean',
    'throughput_mbps': 'mean'
}).reset_index()

print("\nDaily Trends:")
print(daily_trend)

# ----------------------------------
# 3. Anomaly Detection
# ----------------------------------
# Threshold-based
alerts = df[(df['latency_ms'] > 70) | (df['packet_loss'] > 1)]

print("\nDetected Anomalies:")
print(alerts)

# Z-score method (optional)
df['latency_zscore'] = (df['latency_ms'] - df['latency_ms'].mean()) / df['latency_ms'].std()
z_anomalies = df[df['latency_zscore'] > 2]

print("\nZ-score Anomalies:")
print(z_anomalies)

# ----------------------------------
# 4. Visualization
# ----------------------------------

# 1. Latency Trend Over Time
plt.figure()
for tower in df['tower_id'].unique():
    subset = df[df['tower_id'] == tower]
    plt.plot(subset['timestamp'], subset['latency_ms'], label=tower)

plt.title("Latency Trend (Multi-Day)")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Packet Loss Trend
plt.figure()
for tower in df['tower_id'].unique():
    subset = df[df['tower_id'] == tower]
    plt.plot(subset['timestamp'], subset['packet_loss'], label=tower)

plt.title("Packet Loss Trend")
plt.xlabel("Time")
plt.ylabel("Packet Loss")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Throughput Trend
plt.figure()
for tower in df['tower_id'].unique():
    subset = df[df['tower_id'] == tower]
    plt.plot(subset['timestamp'], subset['throughput_mbps'], label=tower)

plt.title("Throughput Trend")
plt.xlabel("Time")
plt.ylabel("Throughput (Mbps)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Latency vs Packet Loss
plt.figure()
plt.scatter(df['latency_ms'], df['packet_loss'])
plt.title("Latency vs Packet Loss")
plt.xlabel("Latency")
plt.ylabel("Packet Loss")
plt.show()

# ----------------------------------
# 5. Engineering Report
# ----------------------------------
report = {
    "total_records": len(df),
    "total_towers": df['tower_id'].nunique(),
    "avg_latency": df['latency_ms'].mean(),
    "max_latency": df['latency_ms'].max(),
    "avg_packet_loss": df['packet_loss'].mean(),
    "worst_tower": df.groupby('tower_id')['latency_ms'].mean().idxmax()
}

print("\nEngineering Summary Report:")
for k, v in report.items():
    print(f"{k}: {v}")
