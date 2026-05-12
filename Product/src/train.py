import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from src.encoding import Encoder
from src.feature_engineering import FeatureEngineer
from src.config import DATA_PATH, MODEL_PATH, FE_PATH

TARGET = "Exited"

df = pd.read_csv(DATA_PATH)

# STEP 1 — data prep
df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], errors='ignore')

# STEP 2 — split
y = df[TARGET]
X = df.drop(columns=[TARGET])

# STEP 3 — encoding
encoder = Encoder()
X = encoder.transform(X)

# STEP 4 — split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# feature engineering
fe = FeatureEngineer()
fe.fit(X_train)

X_train = fe.transform(X_train)
X_test = fe.transform(X_test)

# model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)

# save
joblib.dump(model, MODEL_PATH)
joblib.dump(fe, FE_PATH)

print("✅ Training complete. Artifacts saved.")