import pandas as pd
import re
from pathlib import Path

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATASET_DIR = BASE_DIR / "datasets" / "raw"
CLEANED_DATASET_DIR = BASE_DIR / "datasets" / "cleaned"

CLEANED_DATASET_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# FILE PATHS
# =========================================================

DATASET_1_PATH = RAW_DATASET_DIR / "IT Support Ticket Data.csv"
DATASET_2_PATH = RAW_DATASET_DIR / "dataset-tickets-multi-lang-4-20k.csv"

# =========================================================
# TEXT CLEANING
# =========================================================

def clean_text(text: str) -> str:
    """
    Basic text cleaning for ticket content.
    """

    if pd.isna(text):
        return ""

    text = text.lower()

    # remove URLs
    text = re.sub(r"http\\S+", "", text)

    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9\\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\\s+", " ", text).strip()

    return text

# =========================================================
# PRIORITY NORMALIZATION
# =========================================================

def normalize_priority(priority: str) -> str:

    if pd.isna(priority):
        return "MEDIUM"

    priority = str(priority).lower()

    if priority in ["low", "p4", "minor"]:
        return "LOW"

    elif priority in ["medium", "moderate", "p3"]:
        return "MEDIUM"

    elif priority in ["high", "important", "p2"]:
        return "HIGH"

    elif priority in ["critical", "urgent", "p1"]:
        return "CRITICAL"

    return "MEDIUM"

# =========================================================
# DEPARTMENT NORMALIZATION
# =========================================================

def normalize_department(text: str) -> str:

    if pd.isna(text):
        return None

    text = str(text).lower()

    # ==========================================
    # NETWORK TEAM
    # ==========================================

    if (
        "network" in text
        or "wifi" in text
        or "internet" in text
        or "router" in text
    ):
        return "NETWORK_TEAM"

    # ==========================================
    # SECURITY TEAM
    # ==========================================

    elif (
        "vpn" in text
        or "password" in text
        or "login" in text
        or "authentication" in text
        or "access denied" in text
        or "security" in text
    ):
        return "SECURITY_TEAM"

    # ==========================================
    # HARDWARE TEAM
    # ==========================================

    elif (
        "laptop" in text
        or "keyboard" in text
        or "mouse" in text
        or "monitor" in text
        or "hardware" in text
    ):
        return "HARDWARE_TEAM"

    # ==========================================
    # SOFTWARE TEAM
    # ==========================================

    elif (
        "software" in text
        or "application" in text
        or "install" in text
        or "outlook" in text
        or "email" in text
    ):
        return "SOFTWARE_TEAM"

    return "IT_SUPPORT"

# =========================================================
# CATEGORY NORMALIZATION
# =========================================================

def normalize_category(text: str) -> str:

    text = text.lower()

    # VPN FIRST
    if (
        "vpn" in text
        or "anyconnect" in text
        or "forticlient" in text
        or "globalprotect" in text
        or "remote access" in text
        or "secure tunnel" in text
    ):
        return "VPN"

    # PASSWORD SECOND
    elif (
        "password" in text
        or "login" in text
        or "signin" in text
    ):
        return "PASSWORD"

    elif (
        "network" in text
        or "wifi" in text
        or "internet" in text
    ):
        return "NETWORK"

    elif (
        "email" in text
        or "outlook" in text
    ):
        return "EMAIL"

    elif (
        "hardware" in text
        or "laptop" in text
        or "keyboard" in text
        or "mouse" in text
    ):
        return "HARDWARE"

    elif (
        "software" in text
        or "application" in text
        or "install" in text
    ):
        return "SOFTWARE"

    return None

# =========================================================
# DATASET 1 CLEANING
# =========================================================

def clean_dataset_1():

    print("Loading Dataset 1...")

    df = pd.read_csv(DATASET_1_PATH)

    # remove useless columns
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # rename columns
    df = df.rename(columns={
        "Body": "text",
        "Department": "department",
        "Priority": "priority"
    })

    # keep required columns only
    df = df[["text", "department", "priority"]]

    # remove null text
    df = df.dropna(subset=["text"])

    # clean text
    df["text"] = df["text"].apply(clean_text)

    # normalize labels
    df["priority"] = df["priority"].apply(normalize_priority)
    df["department"] = df["text"].apply(
    normalize_department
)

    # create category column
    df["category"] = df["text"].apply(normalize_category)
    df = df.dropna(subset=["category"])

    return df

# =========================================================
# DATASET 2 CLEANING
# =========================================================

def clean_dataset_2():

    print("Loading Dataset 2...")

    df = pd.read_csv(DATASET_2_PATH)

    # keep English rows only
    if "language" in df.columns:
        df = df[df["language"] == "en"]

    # combine subject + body
    df["text"] = (
        df["subject"].fillna("") + " " +
        df["body"].fillna("")
    )

    # clean text
    df["text"] = df["text"].apply(clean_text)

    # normalize queue → department
    df["department"] = df["text"].apply(
    normalize_department
)

    # normalize priority
    df["priority"] = df["priority"].apply(normalize_priority)

    # normalize category
    df["category"] = df["text"].apply(normalize_category)
    df = df.dropna(subset=["category"])

    # keep required columns
    df = df[["text", "department", "priority", "category"]]

    # remove empty rows
    df = df[df["text"].str.len() > 5]

    return df

# =========================================================
# BUILD FINAL DATASETS
# =========================================================

def build_final_datasets():

    df1 = clean_dataset_1()
    df2 = clean_dataset_2()

    combined_df = pd.concat([df1, df2], ignore_index=True)

    # remove duplicates
    combined_df = combined_df.drop_duplicates()

    # =====================================================
    # CLASSIFICATION DATASET
    # =====================================================

    classification_df = combined_df[["text", "category"]]

    # =====================================================
    # PRIORITY DATASET
    # =====================================================

    priority_df = combined_df[["text", "priority"]]

    # =====================================================
    # ROUTING DATASET
    # =====================================================

    routing_df = combined_df[["text", "department"]]

    # =====================================================
    # SAVE FILES
    # =====================================================

    classification_df.to_csv(
        CLEANED_DATASET_DIR / "classification_dataset.csv",
        index=False
    )

    priority_df.to_csv(
        CLEANED_DATASET_DIR / "priority_dataset.csv",
        index=False
    )

    routing_df.to_csv(
        CLEANED_DATASET_DIR / "routing_dataset.csv",
        index=False
    )

    print("Datasets cleaned successfully!")

# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    build_final_datasets()