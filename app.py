from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import pickle
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load HTML templates
templates = Jinja2Templates(directory="templates")

# Load pipeline
with open("aml_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

model         = pipeline["model"]
columns       = pipeline["columns"]
sender_stats  = pipeline["sender_stats"]   


MEDIAN_TXN_COUNT         = float(sender_stats["sender_txn_count"].median())
MEDIAN_AVG_AMOUNT        = float(sender_stats["sender_avg_amount"].median())
MEDIAN_UNIQUE_RECEIVERS  = float(sender_stats["sender_unique_receivers"].median())


# Request schema
class Transaction(BaseModel):
    amount: float
    country: str
    transaction_type: str
    mode_of_payment: str


# Serve UI
@app.get("/")
def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Prediction endpoint
@app.post("/predict")
def predict(data: Transaction):

    df = pd.DataFrame([data.dict()])

    now = datetime.now()

    # ── Time features (same as training) ──────────────────────────────────
    df["hour"]  = now.hour
    df["day"]   = now.day
    df["month"] = now.month

    # ── Binary risk flags (same as training) ──────────────────────────────
    df["is_large_txn"]        = (df["amount"] > 8000).astype(int)
    df["is_high_risk_country"] = df["country"].isin(["Nigeria", "UAE"]).astype(int)

    # ── Sender behavioural features ───────────────────────────────────────
    # At inference time we have no sender_id, so we use the median values
    # computed from the training set (stored in the pipeline at save time).
    # This is the neutral/average-sender assumption and avoids zeroing out
    # four of the most predictive features.
    df["sender_txn_count"]        = MEDIAN_TXN_COUNT
    df["sender_avg_amount"]       = MEDIAN_AVG_AMOUNT
    df["sender_unique_receivers"] = MEDIAN_UNIQUE_RECEIVERS
    df["time_diff"]               = 0  # no prior transaction to diff against

    # ── Categorical encoding (same as training) ───────────────────────────
    df = pd.get_dummies(df)

    # ── Align columns to training schema ──────────────────────────────────
    df = df.reindex(columns=columns, fill_value=0)

    prob       = model.predict_proba(df)[:, 1][0]
    prediction = int(prob > 0.3)

    return {
        "fraud_probability": float(prob),
        "is_suspicious":     prediction
    }