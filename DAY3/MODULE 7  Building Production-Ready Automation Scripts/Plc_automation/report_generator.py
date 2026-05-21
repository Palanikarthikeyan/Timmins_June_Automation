from collections import Counter

def generate_report(logs, report_path):

    error_count = 0
    warning_count = 0

    equipment_counter = Counter()

    for log in logs:

        equipment_counter[log["equipment"]] += 1

        if log["severity"] == "ERROR":
            error_count += 1

        elif log["severity"] == "WARNING":
            warning_count += 1

    with open(report_path, "w") as report:

        report.write("PLC AUTOMATION REPORT\n")
        report.write("========================\n\n")

        report.write(f"Total Logs     : {len(logs)}\n")
        report.write(f"ERROR Count    : {error_count}\n")
        report.write(f"WARNING Count  : {warning_count}\n\n")

        report.write("Equipment Activity\n")

        for equipment, count in equipment_counter.items():

            report.write(f"{equipment} --> {count} events\n")
