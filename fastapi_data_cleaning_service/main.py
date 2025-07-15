from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
from io import BytesIO
from typing import List

app = FastAPI()

def load_csv(file: UploadFile):
    contents = file.file.read()
    return pd.read_csv(BytesIO(contents))

@app.post("/clean/remove-duplicates")
async def remove_duplicates(file: UploadFile = File(...)):
    df = load_csv(file)
    df_clean = df.drop_duplicates()
    return {"rows_before": len(df), "rows_after": len(df_clean)}

@app.post("/clean/missing-values")
async def handle_missing_values(method: str = Form(...), file: UploadFile = File(...)):
    df = load_csv(file)
    if method == "mean":
        df.fillna(df.mean(numeric_only=True), inplace=True)
    elif method == "median":
        df.fillna(df.median(numeric_only=True), inplace=True)
    elif method == "drop":
        df.dropna(inplace=True)
    else:
        return {"error": "Invalid method. Choose mean, median, or drop."}
    return {"rows": len(df), "columns": list(df.columns)}

@app.post("/clean/standardize-columns")
async def standardize_columns(file: UploadFile = File(...)):
    df = load_csv(file)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return {"standardized_columns": list(df.columns)}

@app.post("/clean/validate-schema")
async def validate_schema(expected_columns: List[str] = Form(...), file: UploadFile = File(...)):
    df = load_csv(file)
    missing = set(expected_columns) - set(df.columns)
    extra = set(df.columns) - set(expected_columns)
    return {
        "expected_columns": expected_columns,
        "actual_columns": list(df.columns),
        "missing_columns": list(missing),
        "extra_columns": list(extra)
    }
