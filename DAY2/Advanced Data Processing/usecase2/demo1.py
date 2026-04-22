import pandas as pd

# Load data
df = pd.read_csv("machine_sensor_data.csv")

# Clean spaces in unit columns
df['pressure_unit'] = df['pressure_unit'].str.strip()

# -------------------------------
# Temperature Normalization → Celsius
# -------------------------------
def convert_temp(value, unit):
    if unit == 'C':
        return value
    elif unit == 'F':
        return (value - 32) * 5/9
    elif unit == 'K':
        return value - 273.15

df['temp_C'] = df.apply(lambda x: convert_temp(x['temperature'], x['temp_unit']), axis=1)

# -------------------------------
# Pressure Normalization → Pascal
# -------------------------------
def convert_pressure(value, unit):
    if unit == 'Pa':
        return value
    elif unit == 'kPa':
        return value * 1000
    elif unit == 'bar':
        return value * 100000
    elif unit == 'psi':
        return value * 6894.76

df['pressure_Pa'] = df.apply(lambda x: convert_pressure(x['pressure'], x['pressure_unit']), axis=1)

# -------------------------------
# Vibration Normalization → mm/s
# -------------------------------
def convert_vibration(value, unit):
    if unit == 'mm/s':
        return value
    elif unit == 'um/s':
        return value / 1000

df['vibration_mm_s'] = df.apply(lambda x: convert_vibration(x['vibration'], x['vibration_unit']), axis=1)

# -------------------------------
# Final Clean Dataset
# -------------------------------
normalized_df = df[['machine_id', 'process', 'temp_C', 'pressure_Pa', 'vibration_mm_s']]

print("\nNormalized Sensor Data:")
print(normalized_df)
