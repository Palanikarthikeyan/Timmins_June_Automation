import re

def read_plc_logs(file_path):

    parsed_logs = []

    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\S+) (.+)"

    with open(file_path, "r") as file:

        for line in file:

            match = re.match(pattern, line)

            if match:

                log_data = {
                    "timestamp": match.group(1),
                    "severity": match.group(2),
                    "equipment": match.group(3),
                    "message": match.group(4)
                }

                parsed_logs.append(log_data)

    return parsed_logs
