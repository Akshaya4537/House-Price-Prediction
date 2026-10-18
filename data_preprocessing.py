import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("../Data Collection/house_data.csv")

encoder = LabelEncoder()
data["Location"] = encoder.fit_transform(data["Location"])

print("Preprocessed Data:")
print(data.to_string(index=False))

data.to_csv("processed_house_data.csv", index=False)
print("\nProcessed data saved successfully!")