import pandas as pd

df = pd.read_csv("usage.csv")

# Pricing rules
CALL_RATE = 0.5     # per minute
DATA_RATE = 0.1     # per MB

# Calculate cost
df['call_cost'] = df['minutes'] * CALL_RATE
df['data_cost'] = df['data_mb'] * DATA_RATE
df['total_cost'] = df['call_cost'] + df['data_cost']

# Aggregate billing
bill = df.groupby("user").agg({
    "total_cost": "sum"
}).reset_index()

# Save report
bill.to_csv("billing_report.csv", index=False)

print("Billing Report Generated")
