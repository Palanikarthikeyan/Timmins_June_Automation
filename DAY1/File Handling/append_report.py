# append_report.py

from datetime import datetime

alarm_count = 3

# Current timestamp
now = datetime.now()

summary_line = (
    f"{now} | Total PLC ALARMS = {alarm_count}\n"
)

# Append into report file
with open("daily_report.txt", "a") as report:

    report.write(summary_line)

print("Summary appended successfully.")
