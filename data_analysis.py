import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Data Collection/house_data.csv")

print("House Price Data Analysis")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nAverage House Price:")
print(data["Price"].mean())

print("\nHighest House Price:")
print(data["Price"].max())

print("\nLowest House Price:")
print(data["Price"].min())

print("\nAverage Price by Location:")
print(data.groupby("Location")["Price"].mean())

data.groupby("Location")["Price"].mean().plot(kind="bar")
plt.title("Average House Price by Location")
plt.xlabel("Location")
plt.ylabel("Average Price")
plt.tight_layout()
plt.show()