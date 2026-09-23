"""Loading and lookup helpers for the processed feature table and model."""

from functools import lru_cache
import os

import joblib
import pandas as pd

from .config import FEATURES_CSV_PATH, FEATURE_COLUMNS, MODEL_PATH


@lru_cache(maxsize=1)
def load_features_table() -> pd.DataFrame:
    return pd.read_csv(FEATURES_CSV_PATH)


def get_app_choices() -> list[str]:
    try:
        return sorted(load_features_table()["app_name"].dropna().astype(str).unique().tolist())
    except FileNotFoundError:
        return []


def lookup_app_features(identifier: str):
    df = load_features_table()
    value = str(identifier).strip().lower()
    app_ids = df["app_id"].astype(str).str.lower() if "app_id" in df.columns else None
    app_names = df["app_name"].astype(str).str.lower() if "app_name" in df.columns else None
    if app_ids is not None and app_names is not None:
        match = df[(app_ids == value) | (app_names == value)]
    elif app_names is not None:
        match = df[app_names == value]
    else:
        match = df[app_ids == value]
    if match.empty:
        return None
    row = match.iloc[0]
    result = {column: row[column] for column in FEATURE_COLUMNS if column in row}
    result["app_id"] = str(row.get("app_id", "")).strip()
    result["app_name"] = str(row.get("app_name", "")).strip()
    return result


@lru_cache(maxsize=1)
def load_model():
    model = joblib.load(MODEL_PATH)
    if hasattr(model, "named_steps") and "classifier" in model.named_steps:
        classifier = model.named_steps["classifier"]
        if not hasattr(classifier, "multi_class"):
            classifier.multi_class = "auto"
    elif not hasattr(model, "multi_class"):
        model.multi_class = "auto"
    return model


def model_available() -> bool:
    return os.path.exists(MODEL_PATH)