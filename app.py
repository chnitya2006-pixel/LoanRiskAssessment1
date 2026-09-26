import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_risk_model.pkl")

st.set_page_config(
    page_title="Loan Risk Assessment",
    page_icon="💰"
)

st.title("💰 Intelligent Loan Risk Assessment System")

st.write("Enter the applicant details below to check loan approval.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

income = st.number_input(
    "Annual Income",
    min_value=0.0,
    value=60000.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=850,
    value=700
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=20000.0
)

loan_duration = st.number_input(
    "Loan Duration (Months)",
    min_value=1,
    max_value=120,
    value=36
)

if st.button("CHECK LOAN RISK"):

    input_data = pd.DataFrame(
        [[
            age,
            income,
            credit_score,
            loan_amount,
            loan_duration
        ]],
        columns=[
            "Age",
            "AnnualIncome",
            "CreditScore",
            "LoanAmount",
            "LoanDuration"
        ]
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ LOAN APPROVED")
    else:
        st.error("❌ LOAN NOT APPROVED")
