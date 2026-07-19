SuperKart — Sales Forecasting MLOps Pipeline
SuperKart is an end‑to‑end MLOps pipeline designed for retail sales forecasting.
The system automates data preparation, model training, artifact management, and application deployment using GitHub Actions, Hugging Face Datasets, Streamlit, and ngrok.

This repository demonstrates a reproducible, cloud‑ready machine learning workflow suitable for enterprise AI teams, academic research, and production deployment.

Overview
SuperKart predicts Product_Store_Sales_Total using:

Product attributes

Store metadata

Pricing information

Location and store type

Core technologies:

XGBoost

Hugging Face Datasets

Streamlit

ngrok

GitHub Actions

Repository Structure
text
SuperKart/
│
├── data/
│   └── SuperKart.csv
│
├── scripts/
│   ├── prep.py
│   └── train.py
│
├── hosting/
│   └── hosting.py
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
Dataset
Hugging Face Dataset:
https://huggingface.co/datasets/JohnPaul13jp79/superkart-dataset

The dataset is uploaded using prep.py and consumed automatically by the training and hosting components.

Model Training
Training script:

text
scripts/train.py
Latest Metrics
RMSE: 289.46

R²: 0.927

Model Artifact
text
xgb_model.pkl
The artifact is uploaded automatically by GitHub Actions for every pipeline run.

MLOps Pipeline (CI/CD)
Workflow definition:

text
.github/workflows/deploy.yml
Pipeline Stages
Install dependencies

Execute prep.py

Execute train.py

Upload model artifact

Deploy Streamlit application

Expose application via ngrok

Output public URL

The pipeline is triggered on every push to the main branch.

Deployment (Streamlit + ngrok)
Deployment script:

text
hosting/hosting.py
Key capabilities:

Local schema loading

Hugging Face schema loading

Interactive user interface

Real‑time prediction

The deployed application is accessible through the ngrok URL generated during CI/CD execution.

Run Locally
bash
git clone https://github.com/johnpaulcdo-spec/SuperKart.git
cd SuperKart
pip install -r requirements.txt
streamlit run hosting/hosting.py
Run in Google Colab
python
from google.colab import userdata
from pyngrok import ngrok
import subprocess

ngrok.set_auth_token(userdata.get("NGROK_TOKEN"))
subprocess.Popen(["streamlit", "run", "hosting/hosting.py", "--server.port=8501"])
public_url = ngrok.connect(8501)
print(public_url)
Usage Example
json
{
  "Product": "Laptop",
  "Store": "Store_42",
  "Price": 799.99,
  "Location": "Urban"
}
Roadmap
Add support for multiple forecasting models

Deploy on AWS, GCP, or Azure

Integrate monitoring and logging

Expand dataset coverage

Add unit tests and CI for model validation

Citation
bibtex
@misc{superkart2026,
  author = {Paul, John},
  title = {SuperKart — Sales Forecasting MLOps Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/johnpaulcdo-spec/SuperKart}}
}
Verifying ngrok Deployment URL
After the CI/CD pipeline deploys the Streamlit application, GitHub Actions prints a public ngrok URL.

Verification Steps
Open GitHub Actions

Select the latest workflow run

Expand the step titled Deploy Streamlit app with ngrok

Confirm the presence of a URL similar to:
https://xxxx.ngrok-free.app

This URL provides access to the live SuperKart forecasting application.
