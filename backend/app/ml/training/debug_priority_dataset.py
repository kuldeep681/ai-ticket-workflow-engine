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
    / "priority_dataset.csv"
)

# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv(DATASET_PATH)

# =========================================================
# PRIORITY COUNTS
# =========================================================

print("\n================ PRIORITY COUNTS ================\n")

print(df["priority"].value_counts())

print("\n=================================================\n")