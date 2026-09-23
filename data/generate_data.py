import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of records
num_samples = 5000

# Generate machine sensor data
temperature = np.random.normal(65, 12, num_samples)
pressure = np.random.normal(5.5, 0.7, num_samples)
vibration = np.random.normal(3, 1.5, num_samples)
current = np.random.normal(12, 2, num_samples)
voltage = np.random.normal(380, 15, num_samples)
operating_hours = np.random.randint(100, 5000, num_samples)

# Determine whether machine failure is likely
failure = (
    (temperature > 85) |
    (vibration > 6) |
    (pressure > 6.5) |
    (operating_hours > 4000)
).astype(int)

# Create DataFrame
data = pd.DataFrame({
    "temperature": temperature.round(2),
    "pressure": pressure.round(2),
    "vibration": vibration.round(2),
    "current": current.round(2),
    "voltage": voltage.round(2),
    "operating_hours": operating_hours,
    "failure": failure
})

# Save CSV
data.to_csv("data/machine_data.csv", index=False)

# Display information
print("====================================")
print("EV BATTERY FACTORY DATASET CREATED")
print("====================================")

print("\nFirst 10 records:")
print(data.head(10))

print("\nDataset shape:")
print(data.shape)

print("\nFailure distribution:")
print(data["failure"].value_counts())

print("\nFile saved as:")
print("data/machine_data.csv")

failure = (
    (temperature > 85) |
    (vibration > 6) |
    (pressure > 6.5) |
    (operating_hours > 4000)
).astype(int)