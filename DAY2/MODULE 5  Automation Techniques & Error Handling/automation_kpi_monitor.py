import pandas as pd
import os
import glob
from datetime import datetime

# Folder paths
INPUT_FOLDER = "logs"
OUTPUT_FOLDER = "output"
LOG_FILE = "process.log"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Logging function
def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# Thresholds
LATENCY_THRESHOLD = 50
PACKET_LOSS_THRESHOLD = 1

all_alerts = []

try:
    # Step 1: Read all CSV files
    files = glob.glob(os.path.join(INPUT_FOLDER, "*.csv"))

    if not files:
        log_message("No files found!")
        print("No files to process.")
        exit()

    print(f"Processing {len(files)} files...\n")

    for file in files:
        try:
            print(f"Reading: {file}")
            df = pd.read_csv(file)

            # Step 2: Detect anomalies
            alerts = df[
                (df['latency_ms'] > LATENCY_THRESHOLD) |
                (df['packet_loss'] > PACKET_LOSS_THRESHOLD)
            ]

            if not alerts.empty:
                alerts['source_file'] = os.path.basename(file)
                all_alerts.append(alerts)

            log_message(f"Processed file: {file}")

        except Exception as e:
            log_message(f"Error processing {file}: {str(e)}")

    # Step 3: Combine all alerts
    if all_alerts:
        final_alerts = pd.concat(all_alerts)

        alert_file = os.path.join(
            OUTPUT_FOLDER,
            f"alerts_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        )

        final_alerts.to_csv(alert_file, index=False)

        print("\n⚠️ ALERTS DETECTED!")
        print(final_alerts)

        log_message(f"Alerts generated: {alert_file}")

    else:
        print("\n✅ No issues detected.")
        log_message("No alerts found.")

except Exception as e:
    log_message(f"Critical error: {str(e)}")
    print("Script failed. Check logs.")
