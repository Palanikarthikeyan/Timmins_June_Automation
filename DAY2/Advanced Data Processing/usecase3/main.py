import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/production_data.csv")

# Create output folders
os.makedirs("output/charts", exist_ok=True)

# -------------------------------
# 1. Data Processing
# -------------------------------
df['yield_%'] = (df['good_chips'] / df['chips_processed']) * 100
df['efficiency'] = df['chips_processed'] / df['uptime_hours']

# -------------------------------
# 2. Summary Table
# -------------------------------
summary = df.groupby(['machine_id', 'shift']).agg(
    total_chips=('chips_processed', 'sum'),
    avg_yield=('yield_%', 'mean'),
    avg_efficiency=('efficiency', 'mean')
).reset_index()

print("\nSummary:")
print(summary)

# Save summary
summary.to_csv("output/summary.csv", index=False)

# -------------------------------
# 3. Visualization
# -------------------------------

# Chart 1: Throughput per Machine
throughput = df.groupby('machine_id')['chips_processed'].sum()

plt.figure()
throughput.plot(kind='bar')
plt.title("Total Throughput per Machine")
plt.xlabel("Machine")
plt.ylabel("Chips Processed")
plt.savefig("output/charts/throughput.png")

# Chart 2: Yield per Machine
yield_data = df.groupby('machine_id')['yield_%'].mean()

plt.figure()
yield_data.plot(kind='bar')
plt.title("Average Yield % per Machine")
plt.xlabel("Machine")
plt.ylabel("Yield %")
plt.savefig("output/charts/yield.png")

# Chart 3: Efficiency vs Downtime
plt.figure()
plt.scatter(df['downtime_hours'], df['efficiency'])
plt.title("Downtime vs Efficiency")
plt.xlabel("Downtime (hours)")
plt.ylabel("Efficiency")
plt.savefig("output/charts/downtime_vs_efficiency.png")

print("\nCharts saved in output/charts/")
