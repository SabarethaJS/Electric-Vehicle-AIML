# EV Type Prediction Chatbot

## Description
This project predicts whether an electric vehicle (EV) is a BEV (Battery Electric Vehicle) or PHEV (Plug-in Hybrid Electric Vehicle) based on Make, Model, Model Year, and Base MSRP using a machine learning model.

## Files
- `train_model.py` : Trains the ML model and saves it as `ev_type_model.pkl`
- `app.py` : Streamlit chatbot for real-time EV type prediction
- `ev_type_model.pkl` : Pre-trained machine learning model
- `EV_Project_PPT.pptx` : Project presentation

## How to Run
1. Install dependencies:
```bash
pip install pandas scikit-learn streamlit

Train the model (if you don’t have ev_type_model.pkl):

python train_model.py


Run the chatbot:

streamlit run app.py
