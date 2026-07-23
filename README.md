# 🏦 Loan Approval Prediction System

A Machine Learning web application built using **Python** and **Streamlit** to predict whether a loan application will be **Approved** or **Rejected** based on applicant details.

---

## 📌 Project Overview

The Loan Approval Prediction System uses a trained Machine Learning model to classify loan applications. Users enter applicant information through a simple Streamlit interface, and the model predicts the loan approval status.

---

## 🚀 Features

- Predict Loan Approval (Approved / Rejected)
- User-friendly Streamlit interface
- Machine Learning classification model
- Data preprocessing with One-Hot Encoding
- Feature Scaling using StandardScaler
- Fast and accurate predictions

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
Loan_Approval_Project/
│── app.py
│── loan_approval_model.pkl
│── scaler.pkl
│── columns.pkl
│── loan_approval.csv
│── README.md
```

---

## 📊 Dataset

The dataset contains the following features:

- name
- city
- income
- credit_score
- loan_amount
- years_employed
- points
- loan_approved (Target Variable)

---

## 🤖 Machine Learning Model

- Algorithm: Logistic Regression
- Problem Type: Binary Classification
- Target Variable: loan_approved
- Model Accuracy: **93%**

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Loan-Approval-Prediction.git
```

Go to the project folder:

```bash
cd Loan-Approval-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📷 Application Workflow

1. Enter applicant details.
2. Click **Predict Loan Approval**.
3. The model predicts whether the loan is approved or rejected.
4. The prediction is displayed on the screen.

---

## 📈 Model Performance

- Accuracy: **93%**
- Evaluation Metrics:
  - Accuracy Score
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

---

## 📦 Requirements

```
streamlit
pandas
scikit-learn
joblib
```

---

## 👩‍💻 Developer

**Shravani Phalke**

---

## 📜 License

This project is developed for educational and learning purposes.
