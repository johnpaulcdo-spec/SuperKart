
import streamlit as st
import pandas as pd

st.title("SuperKart Sales Forecasting 🚀")

st.write("Welcome to the SuperKart demo app!")

# Example: load sample data
data = {'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [100, 120, 90]}
df = pd.DataFrame(data)

st.line_chart(df.set_index('Month'))
