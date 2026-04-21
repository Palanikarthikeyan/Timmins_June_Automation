import pandas as pd

df = pd.read_csv("customers_raw.csv")

# Clean phone numbers
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)

# Normalize names
df['name'] = df['name'].str.strip().str.title()

# Aggregate revenue
summary = df['revenue'].sum()

# Save
df.to_csv("customers_clean.csv", index=False)

print("Total Revenue:", summary)
