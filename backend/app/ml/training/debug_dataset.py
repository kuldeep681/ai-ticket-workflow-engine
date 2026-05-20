import pandas as pd
from pathlib import Path

# =========================================================
# PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = (
    BASE_DIR
    / "datasets"
    / "cleaned"
    / "classification_dataset.csv"
)

# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv(DATASET_PATH)

# =========================================================
# CATEGORY COUNTS
# =========================================================

print("\n================ CATEGORY COUNTS ================\n")

print(df["category"].value_counts())

print("\n=================================================\n")