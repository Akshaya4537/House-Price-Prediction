import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load processed data
data = pd.read_csv("../Data Preprocessing/processed_house_data.csv")

# Separate input and output
X = data.drop("Price", axis=1)
y = data["Price"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict prices
predictions = model.predict(X_test)

# Display results
print("Model Training Completed Successfully!")
print("\nActual Prices:")
print(list(y_test))

print("\nPredicted Prices:")
print(list(predictions))

print("\nMean Absolute Error:")
print(mean_absolute_error(y_test, predictions))