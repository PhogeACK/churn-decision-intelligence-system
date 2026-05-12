from pathlib import Path

# Project root (one level above /src)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = BASE_DIR / "data" / "churn.csv"
MODEL_PATH = BASE_DIR / "models" / "model.pkl"
FE_PATH = BASE_DIR / "models" / "feature_engineer.pkl"