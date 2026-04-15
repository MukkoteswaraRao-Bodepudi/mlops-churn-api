# 🚀 MLOps Churn Prediction API

## 📌 Overview

This project builds an end-to-end Machine Learning pipeline to predict customer churn and deploys it as a production-ready API using FastAPI and Docker.

---

## Run Locally

1. Activate environment:
   source venv/Scripts/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run API:
   uvicorn src.app:app --reload
   
---

## ⚙️ Tech Stack

* Python
* Pandas
* Scikit-learn
* FastAPI
* Docker
* Render (Cloud Deployment)

---

## 🔥 Features

* Data preprocessing pipeline
* Machine learning model (Random Forest)
* REST API for predictions
* Dockerized application
* Deployed on cloud with public access

---

## 🌐 Live API

👉 https://churn-api-of1n.onrender.com

---

## 🧪 API Usage

### Endpoint:

POST `/predict`

### Input:

```json
{
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 800
}
```

### Output:

```json
{
  "status": "success",
  "prediction": 0,
  "result": "No Churn"
}
```

---

## 🐳 Run with Docker

```bash
docker pull mukkoteswararaobodepudi/churn-api
docker run -p 8000:8000 mukkoteswararaobodepudi/churn-api
```

---

## 📁 Project Structure

```
mlops-churn-project/
│── src/
│── models/
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 🎯 Key Learnings

* End-to-end ML pipeline development
* API deployment using FastAPI
* Docker containerization
* Cloud deployment (Render)
* Handling real-world MLOps challenges

---

## 👨‍💻 Author

Mukkoteswara Rao Bodepudi
