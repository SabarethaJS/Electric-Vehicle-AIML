import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample EV data
data = pd.DataFrame({
    'Make': ['Tesla','Tesla','Toyota','Toyota','BMW','BMW'],
    'Model': ['Model S','Model 3','Prius Prime','RAV4 Prime','i3','i8'],
    'Model_Year': [2020,2021,2020,2021,2019,2020],
    'Base_MSRP': [80000,50000,30000,40000,45000,140000],
    'EV_Type': ['BEV','BEV','PHEV','PHEV','BEV','PHEV']
})

# Convert Make and Model into numbers
data_encoded = pd.get_dummies(data, columns=['Make','Model'])
X = data_encoded.drop('EV_Type', axis=1)
y = data_encoded['EV_Type']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the trained model
with open('ev_type_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Model trained and saved as ev_type_model.pkl")
