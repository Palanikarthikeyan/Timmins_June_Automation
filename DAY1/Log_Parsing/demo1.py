import re
from collections import Counter

# Open log file
with open("plc_alarm.log", "r") as file:
    logs = file.readlines()

# Counters
total_logs = 0
error_count = 0
warning_count = 0

# Equipment tracking
equipment_counter = Counter()

# Regex pattern
pattern = "(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\S+) (.+)"

print("\n========= PLC LOG ANALYSIS =========\n")

for line in logs:
    match = re.match(pattern, line)

    if match:
        timestamp = match.group(1)
        severity = match.group(2)
        equipment = match.group(3)
        message = match.group(4)

        total_logs += 1
        equipment_counter[equipment] += 1

        print(f"Time      : {timestamp}")
        print(f"Severity  : {severity}")
        print(f"Equipment : {equipment}")
        print(f"Message   : {message}")
        print("-----------------------------------")

        # Count warnings/errors
        if severity == "ERROR":
            error_count += 1

        elif severity == "WARNING":
            warning_count += 1

# Generate summary report
print("\n========= SUMMARY REPORT =========\n")

print(f"Total Log Entries : {total_logs}")
print(f"Total ERROR Logs  : {error_count}")
print(f"Total WARNING Logs: {warning_count}")

print("\nMost Frequent Equipment Alerts:")

for device, count in equipment_counter.items():
    print(f"{device} --> {count} events")
