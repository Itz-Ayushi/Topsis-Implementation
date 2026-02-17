# Title: TOPSIS – Multiple Criteria Decision Making

---

## 📋 Overview

This project implements **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** for Multi-Criteria Decision Making (MCDM).

The solution is delivered in three formats:

- Command Line Tool  
- PyPI Package with CLI support  
- Flask Web Service with Email functionality  

---

## 1. Methodology

Data Collection → Data Pre-Processing → Normalization → Weight Assignment → Ideal Best/Worst Calculation → Distance Computation → Score Calculation → Ranking


---

## 2. Description

- Number of Alternatives: Based on input dataset  
- Minimum Criteria Required: 2  
- Input Format: CSV / Excel  
- Output: Ranked CSV file  
- Best Alternative: Highest TOPSIS Score  
- Validation:  
  - Numeric criteria columns only  
  - Weights & Impacts count must match criteria  
  - Impacts must be `+` (benefit) or `-` (cost)  

---

## 3. Input / Output

### 📥 Input

- Dataset file (.csv / .xlsx)
  
| Fund Name | P1   | P2   | P3  | P4   | P5   |
|------------|------|------|-----|------|-------|
| M1 | 0.72 | 0.52 | 4.3 | 63   | 17.14 |
| M2 | 0.85 | 0.72 | 4.1 | 40.5 | 11.54 |
| M3 | 0.81 | 0.66 | 3.2 | 38.1 | 10.69 |
| M4 | 0.81 | 0.66 | 4.6 | 64   | 17.52 |
| M5 | 0.74 | 0.55 | 7.0 | 64.5 | 18.20 |
| M6 | 0.91 | 0.83 | 5.3 | 54.1 | 15.29 |
| M7 | 0.82 | 0.67 | 5.4 | 41.0 | 11.97 |
| M8 | 0.74 | 0.55 | 3.9 | 47.7 | 13.22 |


- Weights (e.g., `1,1,1,1,2`)
- Impacts (e.g., `+,+,-,+,+`)

 

### 📤 Output

Generated file includes (result.csv):

| Fund Name | P1   | P2   | P3  | P4   | P5   | Topsis Score | Rank |
|------------|------|------|-----|------|-------|---------------|------|
| M1 | 0.72 | 0.52 | 4.3 | 63.0 | 17.14 | 0.593828911 | 3 |
| M2 | 0.85 | 0.72 | 4.1 | 40.5 | 11.54 | 0.500588932 | 6 |
| M3 | 0.81 | 0.66 | 3.2 | 38.1 | 10.69 | 0.515266887 | 4 |
| M4 | 0.81 | 0.66 | 4.6 | 64.0 | 17.52 | 0.679646753 | 1 |
| M5 | 0.74 | 0.55 | 7.0 | 64.5 | 18.20 | 0.438568760 | 7 |
| M6 | 0.91 | 0.83 | 5.3 | 54.1 | 15.29 | 0.599458847 | 2 |
| M7 | 0.82 | 0.67 | 5.4 | 41.0 | 11.97 | 0.348446927 | 8 |
| M8 | 0.74 | 0.55 | 3.9 | 47.7 | 13.22 | 0.502060287 | 5 |




✔ Highest score → Rank 1  
✖ Incorrect weights/impacts → Validation Error  

---

## 4. Usage
 
 Command Line:
```bash
python topsis.py data.csv "1,1,1,1,2" "+,+,-,+,+" result.csv
```
---
After PyPI Installation:
```bash
topsis data.csv "1,1,1,1,2" "+,+,-,+,+" result.csv
```
---
## 5. Web Service Interface

The Flask Web App allows users to:

- Upload dataset
- Enter weights & impacts
- Provide email ID
- Receive ranked result via email

Run locally:
```bash
cd web_service
pip install -r requirements.txt
python app.py
```

Open in browser:
```bash
http://127.0.0.1:5000
```
---
## 6. Screenshot of the Interface

User Interface-
<img width="983" height="425" alt="image" src="https://github.com/user-attachments/assets/57617a5f-27ff-4e71-b70b-d440471196fa" />


Email output-
<img width="931" height="702" alt="image" src="https://github.com/user-attachments/assets/597638ac-7347-4a55-898d-ca4f125169cd" />

---

## 7. Technologies Used

- Python
- NumPy
- Pandas
- Flask
- Flask-Mail
- PyPI Packaging Tools

---





