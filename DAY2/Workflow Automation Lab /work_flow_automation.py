import pandas as pd
import os
import time
import glob
from datetime import datetime
import smtplib
from email.message import EmailMessage

# -------------------------------
# CONFIGURATION
# -------------------------------
INPUT_FOLDER = "logs"
PROCESSED_FOLDER = "processed"
ALERT_FOLDER = "alerts"
LOG_FILE = "automation.log"

LATENCY_THRESHOLD = 50
PACKET_LOSS_THRESHOLD = 1

CHECK_INTERVAL = 10  # seconds (monitoring interval)

os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(ALERT_FOLDER, exist_ok=True)

# -------------------------------
# LOGGING FUNCTION
# -------------------------------
def log_message(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

# -------------------------------
# EMAIL ALERT (OPTIONAL)
# -------------------------------
def send_email_alert(file_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = '🚨 Telecom Alert'
        msg['From'] = 'your_email@gmail.com'
        msg['To'] = 'receiver@gmail.com'

        msg.set_content(f"Anomaly detected. See attached file: {file_path}")

        with open(file_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='csv', filename="alerts.csv")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@gmail.com', 'your_app_password')
            smtp.send_message(msg)

        log_message("Email alert sent successfully")

    except Exception as e:
        log_message(f"Email error: {str(e)}")

# -------------------------------
# PROCESS SINGLE FILE
# -------------------------------
def process_file(file_path):
    try:
        print(f"\nProcessing: {file_path}")
        df = pd.read_csv(file_path)

        # Basic validation
        required_cols = ['timestamp', 'tower_id', 'latency_ms', 'packet_loss']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing column: {col}")

        # Detect anomalies
        alerts = df[
            (df['latency_ms'] > LATENCY_THRESHOLD) |
            (df['packet_loss'] > PACKET_LOSS_THRESHOLD)
        ]

        if not alerts.empty:
            alert_file = os.path.join(
                ALERT_FOLDER,
                f"alerts_{os.path.basename(file_path)}"
            )

            alerts.to_csv(alert_file, index=False)

            print("Alerts found!")
            print(alerts)

            log_message(f"Alerts generated: {alert_file}")

            # Optional email
            # send_email_alert(alert_file)

        else:
            print(" No issues found")

        # Move processed file
        new_path = os.path.join(PROCESSED_FOLDER, os.path.basename(file_path))
        os.rename(file_path, new_path)

        log_message(f"Processed file: {file_path}")

    except Exception as e:
        log_message(f"Error processing {file_path}: {str(e)}")
        print(f" Error: {e}")

# -------------------------------
# BATCH PROCESSING (INITIAL RUN)
# -------------------------------
def batch_process():
    files = glob.glob(os.path.join(INPUT_FOLDER, "*.csv"))

    if not files:
        print("No files found for batch processing.")
        return

    print(f"\nBatch processing {len(files)} files...")

    for file in files:
        process_file(file)

# -------------------------------
# DIRECTORY MONITORING
# -------------------------------
def monitor_directory():
    print("\nMonitoring directory for new files...")

    processed_files = set()

    while True:
        try:
            files = set(glob.glob(os.path.join(INPUT_FOLDER, "*.csv")))

            new_files = files - processed_files

            for file in new_files:
                process_file(file)
                processed_files.add(file)

            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            log_message(f"Monitoring error: {str(e)}")
            time.sleep(CHECK_INTERVAL)

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print("Starting Workflow Automation Lab")

    # Step 1: Initial batch processing
    batch_process()

    # Step 2: Start monitoring for new files
    monitor_directory()
