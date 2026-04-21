import pandas as pd

rows = []

with open("system.log") as f:
    for line in f:
        parts = line.strip().split(" ", 3)
        timestamp = parts[0] + " " + parts[1]
        level = parts[2]
        message = parts[3]

        rows.append([timestamp, level, message])

df = pd.DataFrame(rows, columns=["timestamp", "level", "message"])

# Filter errors
errors = df[df['level'] == "ERROR"]

# Save structured output
df.to_csv("logs_structured.csv", index=False)
errors.to_csv("errors_only.csv", index=False)

print("Log Processing Done")
