import pandas as pd

data = pd.read_csv("house_data.csv")

print("Complete House Data:")
print(data.to_string(index=False))

print("\nFirst 5 Rows:")
print(data.head())

print("\nData Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nLocation Values:")
print(data["Location"].unique())