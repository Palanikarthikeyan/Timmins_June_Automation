'''
Goal - Parse Logs into Structured Fields
Extract:
date
time
severity
component
message
'''
# Read Sample logs
fobj = open('event_logs.log')
logs = fobj.readlines()
fobj.close()

# Parse each log
for line in logs:

    # Split only first 4 spaces
    parts = line.split(maxsplit=4)

    # Create fields
    date      = parts[0]
    time      = parts[1]
    severity  = parts[2]
    component = parts[3]
    message   = parts[4]

    print("Date      :", date)
    print("Time      :", time)
    print("Severity  :", severity)
    print("Component :", component)
    print("Message   :", message)
    print("-" * 40)
