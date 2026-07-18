📘 SuperKart — Sales Forecasting MLOps Pipeline
https://github.com/johnpaulcdo-spec/SuperKart/actions/workflows/deploy.yml/badge.svg

SuperKart is a complete end‑to‑end MLOps pipeline for retail sales forecasting.
It automates data preparation, model training, artifact versioning, and deployment using GitHub Actions, Hugging Face, Streamlit, and ngrok.

This repository demonstrates a modern, reproducible, cloud‑ready ML workflow suitable for enterprise AI teams, academic submissions, and production deployment.

🚀 Project Overview
SuperKart predicts Product_Store_Sales_Total using:

Product attributes

Store metadata

Pricing information

Location and store type

The pipeline uses:

XGBoost Regressor for forecasting

Hugging Face Datasets for versioned data

Streamlit for interactive UI

ngrok for public hosting

GitHub Actions for CI/CD automation

🧱 Repository Structure
Code
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
📊 Dataset
The dataset is versioned and hosted on Hugging Face:

🔗 Hugging Face Dataset:  
https://huggingface.co/datasets/JohnPaul13jp79/SuperKart_dataset (huggingface.co in Bing)

Uploaded using prep.py and automatically consumed by training and hosting scripts.

🧪 Model Training
Training is performed using scripts/train.py.

Model:
XGBoost Regressor

Latest Metrics:
RMSE: 289.46

R²: 0.927

Artifact:
The trained model is saved as:

Code
xgb_model.pkl
GitHub Actions automatically uploads this artifact for every run.

🧰 MLOps Pipeline (CI/CD)
The CI/CD pipeline is defined in:

Code
.github/workflows/deploy.yml
Pipeline Steps
Install dependencies

Run prep.py

Run train.py

Upload xgb_model.pkl

Deploy Streamlit app

Expose via ngrok

Print public URL

Triggered automatically on every push to main.

🌐 Deployment (Streamlit + ngrok)
The hosting script:

Code
hosting/hosting.py
Provides:

Local schema loading

Hugging Face schema loading

Interactive UI

Real‑time predictions

CI/CD Deployment
GitHub Actions starts Streamlit and exposes it via ngrok:

Code
https://xxxx.ngrok-free.app
The URL appears in the Actions logs under:

Deploy Streamlit app with ngrok

🧪 Testing the Live App
Open the ngrok URL printed in GitHub Actions

Enter product/store details

Click Predict Sales

View forecast results instantly

💻 Run Locally
Clone the repo:

Code
git clone https://github.com/johnpaulcdo-spec/SuperKart.git
cd SuperKart
Install dependencies:

Code
pip install -r requirements.txt
Run the app:

Code
streamlit run hosting/hosting.py
🧪 Run in Colab (Manual Hosting)
Add your ngrok token in:

Colab → Settings → Secrets → NGROK_TOKEN

Then run:

python
from google.colab import userdata
from pyngrok import ngrok
import subprocess

ngrok.set_auth_token(userdata.get("NGROK_TOKEN"))
subprocess.Popen(["streamlit", "run", "hosting/hosting.py", "--server.port=8501"])
public_url = ngrok.connect(8501)
print(public_url)
🏗 Docker Deployment (Optional)
A Dockerfile is included for containerized deployment:

Code
docker build -t superkart .
docker run -p 8501:8501 superkart
🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Commit changes

Push and open a PR

Every PR triggers the CI/CD pipeline automatically.

📜 License
This project is open for educational and research use.
