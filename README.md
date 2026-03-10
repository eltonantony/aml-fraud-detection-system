# AML Fraud Detection System

A machine learning system that analyzes financial transactions and predicts whether a transaction is suspicious or normal.

---

## Technology Stack

- Python
- FastAPI
- XGBoost / Scikit-learn
- Docker
- HTML / JavaScript
- Pandas

---

## Project Structure

```
aml-fraud-detection/
│
├── main.py                  
├── aml_pipeline.pkl         
├── requirements.txt         
├── Dockerfile               
├── docker-compose.yml       
│
└── templates/
      └── index.html         
```

---

## Running the Project

### Docker Compose

```bash
docker compose up --build
```

### Docker

```bash
docker build -t aml-api .
docker run -p 8000:8000 aml-api
```

### Without Docker

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000` in your browser.

---

## API

Swagger docs available at `http://localhost:8000/docs`

### POST /predict

Request:
```json
{
  "amount": 9000,
  "country": "UAE",
  "transaction_type": "transfer",
  "mode_of_payment": "crypto"
}
```

Response:
```json
{
  "fraud_probability": 0.82,
  "is_suspicious": 1
}
```

---

## Author

Elton Antony

---

## License

This project is for educational and demonstration purposes only.
