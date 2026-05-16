'''
Filter Only ERROR Events
Goal
Print only:
ERROR logs
component names
'''
fobj = open('events_logs.log')
logs = fobj.readlines()
fobj.close()

print("ERROR Components:")
print()

for line in logs:

    parts = line.split(maxsplit=4)

    severity = parts[2]
    component = parts[3]

    # Filter only ERROR logs
    if severity == "ERROR":

        print(component)
