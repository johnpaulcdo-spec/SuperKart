# 📘 SuperKart — Sales Forecasting MLOps Pipeline

![CI/CD](https://github.com/johnpaulcdo-spec/SuperKart/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-Educational%20Use-lightgrey.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

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

```text
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
