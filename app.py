from flask import Flask, request
import pandas as pd
import numpy as np
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ---------------- CONFIGURE EMAIL ----------------
SENDER_EMAIL = "asingh56_be23@thapar.edu"   
SENDER_PASSWORD = "sczm zcne othp mjfy"  
# ------------------------------------------------------


@app.route('/')
def home():
    return '''
    <h2>TOPSIS Web Service</h2>
    <form action="/topsis" method="post" enctype="multipart/form-data">
        
        Upload CSV File:<br>
        <input type="file" name="file" required><br><br>

        Weights (comma separated):<br>
        <input type="text" name="weights" placeholder="1,1,1,1,1" required><br><br>

        Impacts (comma separated + or -):<br>
        <input type="text" name="impacts" placeholder="+,+,-,+,+" required><br><br>

        Email:<br>
        <input type="text" name="email" placeholder="example@gmail.com" required><br><br>

        <input type="submit" value="Submit">
    </form>
    '''


@app.route('/topsis', methods=['POST'])
def calculate_topsis():
    try:
        file = request.files['file']
        weights_input = request.form['weights']
        impacts_input = request.form['impacts']
        email = request.form['email']

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Error: Invalid email format."

        if file.filename == '':
            return "Error: No file selected."

        input_path = "input.csv"
        file.save(input_path)

        df = pd.read_csv(input_path)

        if df.shape[1] < 3:
            return "Error: Input file must contain at least 3 columns."

        try:
            weights = list(map(float, weights_input.split(',')))
        except:
            return "Error: Weights must be numeric and comma separated."

        impacts = impacts_input.split(',')

        num_criteria = df.shape[1] - 1

        if len(weights) != num_criteria or len(impacts) != num_criteria:
            return "Error: Number of weights, impacts and criteria columns must be same."

        for impact in impacts:
            if impact not in ['+', '-']:
                return "Error: Impacts must be either '+' or '-'."

        for col in df.columns[1:]:
            if not pd.api.types.is_numeric_dtype(df[col]):
                return "Error: From 2nd column onwards must contain numeric values."

        data = df.iloc[:, 1:].values.astype(float)

        # STEP 1: Normalize
        norm = np.sqrt((data ** 2).sum(axis=0))
        normalized = data / norm

        # STEP 2: Weighted
        weighted = normalized * weights

        # STEP 3: Ideal best & worst
        ideal_best = []
        ideal_worst = []

        for i in range(len(impacts)):
            if impacts[i] == '+':
                ideal_best.append(np.max(weighted[:, i]))
                ideal_worst.append(np.min(weighted[:, i]))
            else:
                ideal_best.append(np.min(weighted[:, i]))
                ideal_worst.append(np.max(weighted[:, i]))

        ideal_best = np.array(ideal_best)
        ideal_worst = np.array(ideal_worst)

        # STEP 4: Distance
        d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
        d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

        # STEP 5: Score
        score = d_worst / (d_best + d_worst)

        df['Topsis Score'] = score
        df['Rank'] = df['Topsis Score'].rank(method='max', ascending=False).astype(int)

        output_path = "result.csv"
        df.to_csv(output_path, index=False)

        # ---------------- SEND EMAIL ----------------

        msg = EmailMessage()
        msg['Subject'] = "Your TOPSIS Result"
        msg['From'] = SENDER_EMAIL
        msg['To'] = email
        msg.set_content("Please find attached your TOPSIS result file.")

        with open(output_path, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data,
                               maintype='application',
                               subtype='octet-stream',
                               filename="result.csv")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        return "TOPSIS calculated successfully! Result sent to your email."

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
