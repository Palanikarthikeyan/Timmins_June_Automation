'''
Goal -  Extract Only Messages
Print only operator messages.
'''
fobj = open('event_logs.log')
logs = fobj.readlines()
fobj.close()

for line in logs:

    parts = line.split(maxsplit=4)

    message = parts[4]

    print(message)
