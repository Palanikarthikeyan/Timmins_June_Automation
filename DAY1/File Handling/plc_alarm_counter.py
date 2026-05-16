# plc_alarm_counter.py

alarm_count = 0

# Open the log file in read mode
with open("plc_alarm.log", "r") as file:

    # Read line by line
    for line in file:

        # Check whether ALARM exists in line
        if "ALARM" in line:
            alarm_count += 1

# Print result
print("Total ALARM events:", alarm_count)
