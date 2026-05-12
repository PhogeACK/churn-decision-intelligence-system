from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
from fastapi import UploadFile, File
import io
from fastapi.responses import StreamingResponse

from src.predict import predict

app = FastAPI()


# -----------------------
# Input Schema
# -----------------------

class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Complain: int
    Satisfaction_Score: int
    Card_Type: str
    Point_Earned: int


# -----------------------
# Routes
# -----------------------

@app.get("/")
def home():
    return {"message": "Churn Decision API is running"}


@app.post("/predict")
def predict_customers(customers: List[Customer]):
    df = pd.DataFrame([c.dict() for c in customers])
    results = predict(df)
    return results

@app.post("/predict-file")
def predict_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        results = predict(df)
        results_df = pd.DataFrame(results)

        stream = io.StringIO()
        results_df.to_csv(stream, index=False)
        stream.seek(0)

        return StreamingResponse(
            iter([stream.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=predictions.csv"}
        )

    except Exception as e:
        return {"error": str(e)}