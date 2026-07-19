# 📘 SuperKart — Sales Forecasting MLOps Pipeline

`https://github.com/johnpaulcdo-spec/SuperKart/actions/workflows/deploy.yml/badge.svg`

SuperKart is a complete **end‑to‑end MLOps pipeline** for retail sales forecasting.  
It automates data preparation, model training, artifact versioning, and deployment using **GitHub Actions**, **Hugging Face**, **Streamlit**, and **ngrok**.

This repository demonstrates a modern, reproducible, cloud‑ready ML workflow suitable for enterprise AI teams, academic submissions, and production deployment.

---

## 🚀 Project Overview

SuperKart predicts **Product_Store_Sales_Total** using:

- Product attributes  
- Store metadata  
- Pricing information  
- Location and store type  

The pipeline uses:

- XGBoost Regressor  
- Hugging Face Datasets  
- Streamlit  
- ngrok  
- GitHub Actions  

---

## 🧱 Repository Structure
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
---

## 📊 Dataset

🔗 **Hugging Face Dataset:**  
https://huggingface.co/datasets/JohnPaul13jp79/SuperKart_dataset

Uploaded using `prep.py` and automatically consumed by training and hosting scripts.
---

## 🧪 Model Training

Training is performed using:

scripts/train.py

### Model  
XGBoost Regressor

### Latest Metrics

- **RMSE:** 289.46  
- **R²:** 0.927  

### Artifact

xgb_model.pkl

GitHub Actions automatically uploads this artifact for every run.
---

## 🧰 MLOps Pipeline (CI/CD)

Defined in:

.github/workflows/deploy.yml

### Pipeline Steps

1. Install dependencies  
2. Run `prep.py`  
3. Run `train.py`  
4. Upload model artifact  
5. Deploy Streamlit app  
6. Expose via ngrok  
7. Print public URL  

Triggered automatically on every push to `main`.
---
## 🌐 Deployment (Streamlit + ngrok)

Deployment is triggered automatically on every push to the `main` branch.

**Hosting script:**
- `hosting/hosting.py`
- Accessible via: [https://xxxx.ngrok-free.app](https://xxxx.ngrok-free.app)

**Features provided:**
- Local schema loading
- Hugging Face schema loading
- Interactive UI
- Real-time predictions

---

## 🧪 Testing the Live App

1. Open the ngrok URL printed in GitHub Actions  
2. Enter product/store details  
3. Click **Predict Sales**  
4. View forecast results  

---

## 💻 Run Locally

```bash
git clone https://github.com/johnpaulcdo-spec/SuperKart.git
cd SuperKart
pip install -r requirements.txt
streamlit run hosting/hosting.py
---

## 🧪 Run in Colab (Manual Hosting)

```python
from google.colab import userdata
from pyngrok import ngrok
import subprocess

ngrok.set_auth_token(userdata.get("NGROK_TOKEN"))
subprocess.Popen(["streamlit", "run", "hosting/hosting.py", "--server.port=8501"])
public_url = ngrok.connect(8501)
print(public_url)
---

## 🏷️ Badges

![CI/CD](https://github.com/johnpaulcdo-spec/SuperKart/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-Educational%20Use-lightgrey.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

---

## 📖 Usage Examples

### Example Input
```json
{
  "Product": "Laptop",
  "Store": "Store_42",
  "Price": 799.99,
  "Location": "Urban"
}
---

## 🙏 Acknowledgments

This project builds on the amazing work of:
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Streamlit](https://streamlit.io/)
- [ngrok](https://ngrok.com/)
- [XGBoost](https://xgboost.readthedocs.io/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 🛤 Roadmap

- [ ] Add support for multiple forecasting models  
- [ ] Deploy on cloud platforms (AWS/GCP/Azure)  
- [ ] Integrate monitoring and logging  
- [ ] Expand dataset coverage  
- [ ] Add unit tests and CI for model validation  

---

## 📸 Screenshots

![SuperKart UI](docs/superkart_ui.png)
![Prediction Example](docs/prediction_example.png)

---

## 📜 Citation

If you use SuperKart in academic work, please cite:

```bibtex
@misc{superkart2026,
  author = {Paul, John},
  title = {SuperKart — Sales Forecasting MLOps Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/johnpaulcdo-spec/SuperKart}}
}
