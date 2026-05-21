import json

from plc_reader import read_plc_logs
from report_generator import generate_report
from logger_setup import setup_logger

# Setup logger
logging = setup_logger()

# Load configuration
with open("config.json", "r") as config_file:

    config = json.load(config_file)

try:

    logging.info("PLC Automation Started")

    # Read logs
    logs = read_plc_logs(config["log_file"])

    logging.info(f"{len(logs)} logs processed")

    # Generate report
    generate_report(logs, config["report_file"])

    logging.info("Summary report generated successfully")

    print("Automation completed successfully.")

except Exception as e:

    logging.error(f"Application Failed: {e}")

    print("Error occurred. Check app.log")
