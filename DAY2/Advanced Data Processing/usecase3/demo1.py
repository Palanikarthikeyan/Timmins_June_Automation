'''
Production Throughput Analysis (Grouping + Summarization)
Business Problem
Track number of chips processed per machine per shift.
'''
import pandas as pd

df = pd.DataFrame({
    "machine": ["ETCH01", "ETCH01", "ETCH02", "ETCH02"],
    "shift": ["Day", "Night", "Day", "Night"],
    "chips_processed": [500, 450, 600, 580]
})

summary = df.groupby(["machine", "shift"])["chips_processed"].sum()

print(summary)
