import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
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

# Evaluate on the held-out test set
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R2: {r2:.3f}")

# Persist metrics so downstream steps (e.g. README updates) can read them
with open("metrics.txt", "w") as f:
    f.write(f"RMSE: {rmse:.2f}\n")
    f.write(f"R2: {r2:.3f}\n")

# Save model artifact
joblib.dump(model, "xgb_model.pkl")
print("✅ Model training complete. Saved as xgb_model.pkl")
