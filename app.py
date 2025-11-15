import streamlit as st
import pandas as pd
import pickle

# Load model and encoder
with open('ev_type_model.pkl', 'rb') as f:
    clf, encoder = pickle.load(f)

st.title("EV Type Prediction Chatbot")
st.write("Enter EV details to predict whether it is BEV or PHEV")

# Input fields
make = st.text_input("Make")
model = st.text_input("Model")
year = st.number_input("Model Year", min_value=2000, max_value=2030, value=2022)
msrp = st.number_input("Base MSRP", min_value=0, value=50000)

if st.button("Predict EV Type"):
    # Encode input
    input_df = pd.DataFrame([[make, model, year, msrp]], columns=['Make','Model','Model_Year','Base_MSRP'])
    input_encoded = pd.DataFrame(encoder.transform(input_df[['Make','Model']]).toarray())
    input_final = pd.concat([input_encoded, input_df[['Model_Year','Base_MSRP']].reset_index(drop=True)], axis=1)
    
    prediction = clf.predict(input_final)[0]
    st.success(f"The EV Type is: {prediction}")
