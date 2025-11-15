import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('ev_type_model.pkl', 'rb') as f:
    clf = pickle.load(f)

st.title("🚗 EV Type Prediction Chatbot")
st.write("Predict whether an EV is BEV or PHEV")

# User input
make = st.selectbox("Select Make", ["Tesla","Toyota","BMW"])
model = st.selectbox("Select Model", ["Model S","Model 3","Prius Prime","RAV4 Prime","i3","i8"])
year = st.number_input("Enter Model Year", 2000, 2030, 2021)
msrp = st.number_input("Enter Base MSRP ($)", 10000, 200000, 50000)

if st.button("Predict EV Type"):
    # Define all columns used during training
    columns = ['Model_Year','Base_MSRP',
               'Make_BMW','Make_Tesla','Make_Toyota',
               'Model_Model S','Model_Model 3','Model_Prius Prime',
               'Model_RAV4 Prime','Model_i3','Model_i8']
    
    # Create input DataFrame with all zeros
    input_df = pd.DataFrame(0, index=[0], columns=columns)
    
    # Fill in user input
    input_df['Model_Year'] = year
    input_df['Base_MSRP'] = msrp
    input_df[f'Make_{make}'] = 1
    input_df[f'Model_{model}'] = 1
    
    # Predict
    prediction = clf.predict(input_df)[0]
    st.success(f"The predicted EV Type is: {prediction}")
