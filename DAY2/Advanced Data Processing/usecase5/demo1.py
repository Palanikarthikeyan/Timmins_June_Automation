import pandas as pd
import json

# Load JSON
with open("network.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Aggregate
summary = df.groupby("tower_id").agg({
    "latency": "mean",
    "packet_loss": "mean"
}).reset_index()

# Save
summary.to_json("network_summary.json", orient="records", indent=2)

print("Network KPI Aggregation Done")
