# Title: TOPSIS – Multiple Criteria Decision Making

---

## 1. Methodology

Data Collection → Data Pre-Processing → Normalization → Weight Assignment → Ideal Best/Worst Calculation → Distance Computation → Score Calculation → Ranking

---

## 📋 Overview

TOPSIS ranks alternatives by measuring their closeness to the ideal best solution and distance from the ideal worst solution.

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
- Weights (e.g., `1,1,1,1,2`)
- Impacts (e.g., `+,+,-,+,+`)

### 📤 Output

Generated file includes:

| Alternative | Topsis Score | Rank |
|-------------|--------------|------|
| A1 | 0.5917 | 1 |
| A2 | 0.5840 | 2 |
| A3 | 0.4489 | 3 |

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

-Upload dataset
-Enter weights & impacts
-Provide email ID
-Receive ranked result via email

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
<img width="397" height="448" alt="image" src="https://github.com/user-attachments/assets/0cb30009-7b3b-4126-a9a6-c4925293a94d" />

Email output-
<img width="931" height="702" alt="image" src="https://github.com/user-attachments/assets/597638ac-7347-4a55-898d-ca4f125169cd" />

---

## 7. Technologies Used

-Python
-NumPy
-Pandas
-Flask
-Flask-Mail
-PyPI Packaging Tools

---





