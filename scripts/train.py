import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load prepared dataset
df = pd.read_csv("data/superkart_sales.csv")

# Features and target
X = df.drop("sales", axis=1)
y = df["sales"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

# Save model artifact
joblib.dump(model, "xgb_model.pkl")
print("✅ Model training complete. Saved as xgb_model.pkl")
