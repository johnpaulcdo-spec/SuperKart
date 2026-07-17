import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("xgb_model.pkl")

st.title("🚀 SuperKart Sales Forecasting")

# User input form
st.sidebar.header("Input Features")
feature1 = st.sidebar.number_input("Feature 1", value=0.0)
feature2 = st.sidebar.number_input("Feature 2", value=0.0)
feature3 = st.sidebar.number_input("Feature 3", value=0.0)

# Create dataframe from inputs
input_df = pd.DataFrame([[feature1, feature2, feature3]],
                        columns=["feature1", "feature2", "feature3"])

# Prediction
prediction = model.predict(input_df)[0]
st.metric(label="Predicted Sales", value=f"{prediction:.2f}")
