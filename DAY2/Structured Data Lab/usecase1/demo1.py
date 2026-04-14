'''
Semiconductor Tool Log Parsing (Log → Structured Format)
Business Problem
Fabrication tools generate logs like:
2026-04-14 10:00:01 TOOL=ETCH01 STATUS=RUN TEMP=210
2026-04-14 10:05:15 TOOL=ETCH01 STATUS=ERROR CODE=E101

Need to convert into structured CSV/JSON.
'''
import re
import pandas as pd

logs = [
    "2026-04-14 10:00:01 TOOL=ETCH01 STATUS=RUN TEMP=210",
    "2026-04-14 10:05:15 TOOL=ETCH01 STATUS=ERROR CODE=E101"
]

parsed_logs = []

for log in logs:
    tool = re.search(r"TOOL=(\w+)", log).group(1)
    status = re.search(r"STATUS=(\w+)", log).group(1)

    temp_match = re.search(r"TEMP=(\d+)", log)
    code_match = re.search(r"CODE=(\w+)", log)

    parsed_logs.append({
        "tool": tool,
        "status": status,
        "temperature": temp_match.group(1) if temp_match else None,
        "error_code": code_match.group(1) if code_match else None
    })

df = pd.DataFrame(parsed_logs)
print(df)
