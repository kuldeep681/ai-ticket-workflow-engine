import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = (
    BASE_DIR
    / "datasets"
    / "cleaned"
    / "routing_dataset.csv"
)

df = pd.read_csv(DATASET_PATH)

print(df["department"].value_counts())