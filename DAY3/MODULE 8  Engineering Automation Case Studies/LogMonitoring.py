import re
from collections import Counter

# Open telecom log file
with open("tower_logs.log", "r") as file:
    logs = file.readlines()

# Counters
error_count = 0
warning_count = 0

tower_counter = Counter()

# Regex pattern
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\S+) (\w+) (.+)"

print("\n===== TELECOM NETWORK MONITOR =====\n")

for line in logs:

    match = re.match(pattern, line)

    if match:

        timestamp = match.group(1)
        tower = match.group(2)
        severity = match.group(3)
        message = match.group(4)

        tower_counter[tower] += 1

        print(f"Time      : {timestamp}")
        print(f"Tower     : {tower}")
        print(f"Severity  : {severity}")
        print(f"Message   : {message}")
        print("--------------------------------")

        # Alert detection
        if severity == "ERROR":

            error_count += 1

            print(f"ALERT: Critical issue detected at {tower}")

        elif severity == "WARNING":

            warning_count += 1

print("\n===== SUMMARY REPORT =====\n")

print(f"Total ERROR Events   : {error_count}")
print(f"Total WARNING Events : {warning_count}")

print("\nTower Activity Summary")

for tower, count in tower_counter.items():
    print(f"{tower} --> {count} events")
