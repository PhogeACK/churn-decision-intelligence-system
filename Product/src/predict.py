import pandas as pd
import joblib

from src.config import MODEL_PATH, FE_PATH
from src.encoding import Encoder
from src.decision_logic import segment_customer, get_action, expected_value

# load artifacts
model = joblib.load(MODEL_PATH)
fe = joblib.load(FE_PATH)
encoder = Encoder()


def predict(df):
    df = df.copy()

    # same rename if needed
    df = df.rename(columns={
        "Satisfaction_Score": "Satisfaction Score",
        "Card_Type": "Card Type",
        "Point_Earned": "Point Earned"
    })

    df = df.drop(
    columns=["RowNumber", "CustomerId", "Surname", "Exited"],
    errors="ignore"
    )
    
    # pipeline
    df = encoder.transform(df)
    X = fe.transform(df)

    probs = model.predict_proba(X)[:, 1]

    results = []

    for p in probs:
        segment = segment_customer(p)
        action = get_action(segment)
        ev = expected_value(p, action)

        if ev == 0:
            action = "no_action"

        results.append({
            "probability": round(float(p), 3),
            "segment": segment,
            "action": action,
            "expected_value": ev
        })

    return results


if __name__ == "__main__":
    df = pd.read_csv("data/churn.csv").drop(columns=["Exited"]).head(5)

    results = predict(df)

    for r in results:
        print(r)