# 🛒 SuperKart Sales Forecasting - Streamlit App

## Overview
Interactive Streamlit dashboard serving predictions from the tuned XGBRegressor pipeline.
Users can input product and store details to forecast sales.

## Usage
### CI/CD Deployment
Every push to the `main` branch triggers GitHub Actions:

- Installs dependencies from `requirements.txt`
- Trains and saves the XGBRegressor model (`xgb_model.pkl`)
- Uploads the trained model as an artifact
- Deploys the Streamlit app with ngrok integration
- Prints a public URL in the Actions logs

#### How to find the public URL
1. Go to the **Actions** tab in this repository.
2. Open the latest workflow run.
3. Scroll to the **Deploy Streamlit app with ngrok** step.
4. Copy the printed public URL (e.g., `https://xxxx.ngrok-free.app`) and open it in your browser.

### Run in Google Colab with ngrok
If you want to test the app in Colab and share a public URL:

```python
!pip install streamlit pyngrok datasets joblib xgboost scikit-learn pandas
!python hosting/hosting.py
