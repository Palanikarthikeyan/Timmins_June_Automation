import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("multi_day_kpi_logs.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date

print("\n===== DATA PREVIEW =====")
print(df.head())

# -------------------------------
# 2. Statistical Analysis
# -------------------------------
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# -------------------------------
# 3. Trend Analysis
# -------------------------------
daily_trend = df.groupby('date').agg({
    'latency_ms': 'mean',
    'packet_loss': 'mean',
    'throughput_mbps': 'mean'
}).reset_index()

print("\n===== DAILY TREND =====")
print(daily_trend)

# -------------------------------
# 4. Anomaly Detection
# -------------------------------
# Threshold-based
alerts = df[(df['latency_ms'] > 70) | (df['packet_loss'] > 1)]

print("\n===== ALERTS (THRESHOLD) =====")
print(alerts)

# Z-score method
df['latency_zscore'] = (df['latency_ms'] - df['latency_ms'].mean()) / df['latency_ms'].std()
z_anomalies = df[df['latency_zscore'] > 2]

print("\n===== ALERTS (Z-SCORE) =====")
print(z_anomalies)

# -------------------------------
# 5. Visualization (Matplotlib)
# -------------------------------

# Latency Trend
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

# Packet Loss Trend
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

# Throughput Trend
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

# Scatter Plot
plt.figure()
plt.scatter(df['latency_ms'], df['packet_loss'])
plt.title("Latency vs Packet Loss")
plt.xlabel("Latency (ms)")
plt.ylabel("Packet Loss")
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Seaborn Advanced Visualizations
# -------------------------------

# 1. Heatmap (Correlation)
plt.figure()
corr = df[['latency_ms', 'packet_loss', 'throughput_mbps']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 2. Boxplot (Outlier Detection)
plt.figure()
sns.boxplot(x='tower_id', y='latency_ms', data=df)
plt.title("Latency Distribution per Tower")
plt.show()

# 3. Lineplot (Better Trend Visualization)
plt.figure()
sns.lineplot(data=df, x='timestamp', y='latency_ms', hue='tower_id')
plt.title("Latency Trend (Seaborn)")
plt.xticks(rotation=45)
plt.show()

# 4. Pairplot (Relationship Analysis)
sns.pairplot(df[['latency_ms', 'packet_loss', 'throughput_mbps']])
plt.show()

# -------------------------------
# 7. Engineering Report
# -------------------------------
report = {
    "total_records": len(df),
    "total_towers": df['tower_id'].nunique(),
    "avg_latency": df['latency_ms'].mean(),
    "max_latency": df['latency_ms'].max(),
    "avg_packet_loss": df['packet_loss'].mean(),
    "worst_tower": df.groupby('tower_id')['latency_ms'].mean().idxmax()
}

print("\n===== ENGINEERING REPORT =====")
for k, v in report.items():
    print(f"{k}: {v}")
