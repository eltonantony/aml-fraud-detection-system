# Anti-Money Laundering (AML) Detection System

## Project Overview

This project implements an **Anti-Money Laundering (AML) detection system** using Machine Learning.
The system analyzes financial transaction details and predicts whether a transaction is **suspicious or normal**.

The application includes:

* A **Machine Learning model** for fraud detection
* A **FastAPI backend API** for prediction
* A **web-based user interface (UI)** for entering transaction details
* **Docker containerization** for easy deployment

Users can interact with the system through a **web dashboard**, submit transaction details, and receive **real-time fraud risk predictions**.

---

# Features

* Machine Learning model for detecting suspicious transactions
* FastAPI-based REST API for prediction
* Interactive **web dashboard UI**
* Real-time fraud probability calculation
* Docker containerized deployment
* Automatic API documentation with Swagger UI

---

# Technology Stack

* **Python**
* **FastAPI**
* **Machine Learning (Scikit-learn / XGBoost)**
* **Docker**
* **HTML / JavaScript**
* **Pandas**

---

# Project Structure

```
AML/
│
├── app.py                # FastAPI backend
├── aml_pipeline.pkl      # Trained ML model pipeline
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker container configuration
├── docker-compose.yml    # Docker compose configuration
│
└── templates/
      └── index.html      # Web dashboard UI
```

---

# System Architecture

```
User (Web UI)
      ↓
FastAPI Backend
      ↓
Feature Engineering
      ↓
Machine Learning Model
      ↓
Fraud Risk Prediction
```

---

# Running the Project

## Option 1 – Run with Docker (Recommended)

### Build Docker Image

```
docker build -t aml-api .
```

### Run the Container

```
docker run -p 8000:8000 aml-api
```

### Open the Application

Open your browser and go to:

```
http://localhost:8000
```

You will see the **AML Transaction Detection Dashboard**.

---

## Option 2 – Run with Docker Compose

```
docker compose up --build
```

Then open:

```
http://localhost:8000
```

---

# Using the Application

1. Open the AML dashboard in your browser.
2. Enter transaction details:

   * Transaction Amount
   * Country
   * Transaction Type
   * Payment Method
3. Click **Analyze Transaction**.
4. The system will display:

* Fraud Probability
* Suspicious / Normal transaction status

---

# API Documentation

FastAPI automatically provides API documentation.

Open:

```
http://localhost:8000/docs
```

You can test the `/predict` endpoint directly.

---

# Example Prediction

Example input:

```
Amount: 9000
Country: UAE
Transaction Type: transfer
Payment Mode: crypto
```

Example output:

```
Suspicious Transaction
Fraud Probability: 0.82
```

---

# Future Improvements

* Store transaction history in a database
* Fraud monitoring dashboard
* Authentication system
* Cloud deployment (AWS / GCP / Azure)
* Real-time transaction streaming

---

# Author

Elton Antony

---

# License

This project is for educational and demonstration purposes.
