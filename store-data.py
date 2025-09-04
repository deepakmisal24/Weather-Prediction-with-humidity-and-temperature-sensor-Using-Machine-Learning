import serial
import pandas as pd
from datetime import datetime

# Configure serial port
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with your port (Linux example: '/dev/ttyUSB0')
csv_filename = "data-temperature-humidity.csv"

# Create CSV file with header if it doesn't exist
try:
    df = pd.read_csv(csv_filename)
except FileNotFoundError:
    df = pd.DataFrame(columns=["timestamp", "humidity", "temperature"])
    df.to_csv(csv_filename, index=False)

print("Listening for data... Press Ctrl+C to stop.")

while True:
    line = ser.readline().decode('utf-8').strip()

    if "Failed to read" in line or line.startswith("timestamp"):
        continue

    try:
        parts = line.split(",")
        if len(parts) == 3:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            humidity = float(parts[1])
            temperature = float(parts[2])

            new_data = pd.DataFrame([[timestamp, humidity, temperature]], columns=["timestamp", "humidity", "temperature"])
            new_data.to_csv(csv_filename, mode='a', header=False, index=False)
            print(f"Saved: {timestamp}, {humidity}, {temperature}")

    except Exception as e:
        print(f"Error: {e}")
