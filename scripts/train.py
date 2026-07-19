import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load prepared dataset
df = pd.read_csv("data/SuperKart.csv")

# Features and target
X = df.drop("Product_Store_Sales_Total", axis=1)
y = df["Product_Store_Sales_Total"]

# Mark text columns as categorical so XGBoost can use them natively
categorical_cols = X.select_dtypes(include="object").columns
X[categorical_cols] = X[categorical_cols].astype("category")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    enable_categorical=True,
)
model.fit(X_train, y_train)

# Save model artifact
joblib.dump(model, "xgb_model.pkl")
print("✅ Model training complete. Saved as xgb_model.pkl")
