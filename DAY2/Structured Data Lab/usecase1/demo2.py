'''
Chip Defect Inspection Data (JSON Parsing)
Business Problem

Vision systems inspect chips and produce JSON defect reports.

{
  "chip_id": "CHIP1001",
  "defects": [
    {"type": "scratch", "severity": "high"},
    {"type": "dust", "severity": "low"}
  ]
}

'''
import json

data = '''
{
  "chip_id": "CHIP1001",
  "defects": [
    {"type": "scratch", "severity": "high"},
    {"type": "dust", "severity": "low"}
  ]
}
'''

chip_data = json.loads(data)

print("Chip ID:", chip_data["chip_id"])

for defect in chip_data["defects"]:
    print(defect["type"], defect["severity"])
