'''
Goal Count Severity Types

Count:
INFO
WARNING
ERROR
using  string parsing.
'''
fobj = open('event_logs.log')
logs = fobj.readlines()
fobj.close()

info_count = 0
warning_count = 0
error_count = 0

for line in logs:

    parts = line.split(maxsplit=4)

    severity = parts[2]

    if severity == "INFO":
        info_count += 1

    elif severity == "WARNING":
        warning_count += 1

    elif severity == "ERROR":
        error_count += 1

print("INFO    :", info_count)
print("WARNING :", warning_count)
print("ERROR   :", error_count)
