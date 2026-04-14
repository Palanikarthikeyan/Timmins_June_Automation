'''
1) Wafer Test Data Analysis (CSV Processing + Filtering + Summary)
Business Problem
Semiconductor manufacturing generates wafer probe test results in CSV files.

Engineers need to:
read test data
filter failed dies
calculate yield %
summarize per wafer lot
'''
import pandas as pd

df = pd.read_csv("wafer_test.csv")

# Filter failed dies
failed_dies = df[df["test_result"] == "FAIL"]
print("Failed Dies:")
print(failed_dies)

# Yield calculation
summary = df.groupby("lot_id")["test_result"].value_counts().unstack(fill_value=0)
summary["yield_percent"] = (summary["PASS"] / (summary["PASS"] + summary["FAIL"])) * 100

print("\nLot Summary:")
print(summary)
