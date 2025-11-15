import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset (replace with your actual dataset)
data = pd.DataFrame({
    'Make': ['Tesla', 'Toyota', 'BMW', 'Tesla'],
    'Model': ['Model 3', 'Prius Prime', 'i3', 'Model S'],
    'Model_Year': [2022, 2021, 2020, 2023],
    'Base_MSRP': [55000, 35000, 45000, 80000],
    'EV_Type': ['BEV', 'PHEV', 'BEV', 'BEV']
})

# Features and target
X = data[['Make', 'Model', 'Model_Year', 'Base_MSRP']]
y = data['EV_Type']

# One-hot encode categorical features
encoder = OneHotEncoder()
X_encoded = pd.DataFrame(encoder.fit_transform(X[['Make', 'Model']]).toarray())
X_final = pd.concat([X_encoded, X[['Model_Year', 'Base_MSRP']].reset_index(drop=True)], axis=1)

# Train model
clf = RandomForestClassifier()
clf.fit(X_final, y)

# Save model and encoder
with open('ev_type_model.pkl', 'wb') as f:
    pickle.dump((clf, encoder), f)

print("Model trained and saved as ev_type_model.pkl")
