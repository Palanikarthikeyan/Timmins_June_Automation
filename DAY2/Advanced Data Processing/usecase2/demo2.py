'''
Equipment Sensor Data Normalization (CSV + Data Transformation)
Business Problem
Machines like etching, deposition, lithography tools produce sensor readings in different units.

Need to normalize:
temperature
pressure
vibration
'''
import pandas as pd

df = pd.DataFrame({
    "machine_id": ["ETCH01", "ETCH02", "ETCH03"],
    "temperature_c": [200, 220, 210],
    "pressure_pa": [100000, 120000, 110000]
})

# Normalize values (0 to 1)
df["temp_norm"] = (df["temperature_c"] - df["temperature_c"].min()) / \
                  (df["temperature_c"].max() - df["temperature_c"].min())

df["pressure_norm"] = (df["pressure_pa"] - df["pressure_pa"].min()) / \
                      (df["pressure_pa"].max() - df["pressure_pa"].min())

print(df)
