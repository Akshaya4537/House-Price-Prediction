import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load processed data
data = pd.read_csv("../Data Preprocessing/processed_house_data.csv")

# Separate features and target
X = data.drop("Price", axis=1)
y = data["Price"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Get house details
print("HOUSE PRICE PREDICTION")

area = float(input("📐Enter Area: "))
bathrooms = int(input("🚿Enter Bathrooms: "))
bedrooms = int(input("🛏️Enter Bedrooms: "))
living_area = float(input("🛋️Enter Living Area: "))
kitchen = int(input("🍳Enter Kitchen (1 or 0): "))
swimming_pool = int(input("🏊Swimming Pool (1 or 0): "))
dining_area = int(input("🍽️Dining Area (1 or 0): "))
garage = int(input("🚗Garage (1 or 0): "))
location = input("📍Enter Location: ").strip().title()
road = int(input("🛣️Road Facilities (1 or 0): "))
city = int(input("🏙️City Facilities (1 or 0): "))
garden = int(input("🌸Garden Facilities (1 or 0): "))

house = pd.DataFrame(0, index=[0], columns=X.columns)

values = {
    "Area": area,
    "Bathrooms": bathrooms,
    "Bedrooms": bedrooms,
    "Living_Area": living_area,
    "Kitchen": kitchen,
    "Swimming_Pool": swimming_pool,
    "Dining_Area": dining_area,
    "Garage": garage,
    "Road_Facilities": road,
    "City_Facilities": city,
    "Garden_Facilities": garden
}

for column, value in values.items():
    if column in house.columns:
        house.loc[0, column] = value

location_column = "Location_" + location
if location_column in house.columns:
    house.loc[0, location_column] = 1
else:
    print("Location not found in training data.")

prediction = model.predict(house)
print("\nPredicted House Price:", round(prediction[0], 2))