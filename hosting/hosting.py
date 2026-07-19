import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("xgb_model.pkl")

st.title("🚀 SuperKart Sales Forecasting")

# Sidebar inputs matching the training feature set
st.sidebar.header("Input Features")

product_id = st.sidebar.text_input("Product ID", value="FD1000")
product_weight = st.sidebar.number_input("Product Weight", min_value=0.0, value=12.5, step=0.1)
product_sugar_content = st.sidebar.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
product_allocated_area = st.sidebar.number_input("Product Allocated Area", min_value=0.0, value=0.05, step=0.01)
product_type = st.sidebar.selectbox("Product Type", [
    "Frozen Foods", "Dairy", "Canned", "Baking Goods", "Health and Hygiene",
    "Snack Foods", "Meat", "Household", "Hard Drinks", "Fruits and Vegetables",
    "Breads", "Soft Drinks", "Breakfast", "Starchy Foods", "Others",
])
product_mrp = st.sidebar.number_input("Product MRP", min_value=0.0, value=150.0, step=0.01)
store_id = st.sidebar.selectbox("Store ID", ["OUT001", "OUT002", "OUT003", "OUT004"])
store_establishment_year = st.sidebar.number_input("Store Establishment Year", min_value=1900, max_value=2100, value=2005, step=1)
store_size = st.sidebar.selectbox("Store Size", ["Small", "Medium", "High"])
store_location_city_type = st.sidebar.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
store_type = st.sidebar.selectbox("Store Type", [
    "Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart",
])

# Build input dataframe matching the training column names and order
input_df = pd.DataFrame([{
    "Product_Id": product_id,
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar_content,
    "Product_Allocated_Area": product_allocated_area,
    "Product_Type": product_type,
    "Product_MRP": product_mrp,
    "Store_Id": store_id,
    "Store_Establishment_Year": store_establishment_year,
    "Store_Size": store_size,
    "Store_Location_City_Type": store_location_city_type,
    "Store_Type": store_type,
}])

# Cast text columns to category dtype to match how the model was trained
categorical_cols = input_df.select_dtypes(include="object").columns
input_df[categorical_cols] = input_df[categorical_cols].astype("category")

# Prediction
prediction = model.predict(input_df)[0]
st.metric(label="Predicted Sales", value=f"{prediction:.2f}")
