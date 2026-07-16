"""
SuperKart Sales Forecasting Streamlit App
Loads trained XGBRegressor model from Hugging Face Hub,
collects product/store inputs, and predicts sales.
"""

import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# ✅ Download and load the model from Hugging Face Hub
model_path = hf_hub_download(
    repo_id="JohnPaul13jp79/SuperKart_model",   # Hugging Face repo containing your model
    filename="superkart_xgb_model.pkl"
)
model = joblib.load(model_path)

# ✅ Streamlit UI
st.title("🛒 SuperKart Sales Forecasting")
st.write("Predict product/store sales using the tuned XGBRegressor pipeline.")

# Numeric inputs
product_weight = st.number_input("Product Weight", min_value=0.0, step=0.1)
product_area = st.number_input("Product Allocated Area", min_value=0.0, step=0.1)
product_mrp = st.number_input("Product MRP", min_value=0.0, step=0.1)
store_id = st.number_input("Store ID", min_value=1, step=1)
store_year = st.number_input("Store Establishment Year", min_value=1900, step=1)
store_age = st.number_input("Store Age", min_value=0, step=1)

# Categorical inputs
sugar_content = st.selectbox("Product Sugar Content", ["Low", "Medium", "High"])
product_type = st.selectbox("Product Type", ["Food", "Drink", "Non-Consumable"])
store_size = st.selectbox("Store Size", ["Small", "Medium", "Large"])
store_city = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
store_type = st.selectbox("Store Type", ["Store_Type_1", "Store_Type_2", "Store_Type_3"])

# Prediction button
if st.button("Predict Sales"):
    # ✅ Build input DataFrame
    input_data = pd.DataFrame([{
        "Product_Weight": product_weight,
        "Product_Allocated_Area": product_area,
        "Product_MRP": product_mrp,
        "Store_Id": store_id,
        "Store_Establishment_Year": store_year,
        "Store_Age": store_age,
        "Product_Sugar_Content": sugar_content,
        "Product_Type": product_type,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_city,
        # Encode store type flags
        "Store_Type_1": 1 if store_type == "Store_Type_1" else 0,
        "Store_Type_2": 1 if store_type == "Store_Type_2" else 0,
        "Store_Type_3": 1 if store_type == "Store_Type_3" else 0,
    }])

    # ✅ Run prediction
    prediction = model.predict(input_data)[0]

    # ✅ Display result
    st.success(f"🔮 Predicted Sales: {prediction:.2f}")
