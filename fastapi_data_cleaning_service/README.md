#  FastAPI Data Cleaning as a Service (DaaS)

##  Project Overview
This project offers **Data Cleaning as a Service (DaaS)** through a FastAPI backend. It provides APIs for:
- Removing duplicates
- Handling missing values (mean, median, drop)
- Standardizing column names
- Validating schema against a provided list

##  Installation Steps

```bash
pip install -r requirements.txt
```

##  Running the Application

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

##  API Endpoints

### 1️ POST `/clean/remove-duplicates`
Removes duplicate rows from uploaded CSV.

### 2️ POST `/clean/missing-values`
Handles missing values with method options: mean, median, drop.

### 3️ POST `/clean/standardize-columns`
Standardizes column names to lowercase with underscores.

### 4️ POST `/clean/validate-schema`
Validates uploaded CSV schema against provided columns.

##  Example Use-Cases
- Standardizing datasets for analysis pipelines
- Pre-cleaning data for ML models

##  Future Extensions
- Database integration
- User authentication
- Extended cleaning rules

---
