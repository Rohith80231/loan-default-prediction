import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load('loan_model.pkl')

# Title
st.title('🏦 Loan Default Prediction App')
st.write('Enter loan details below to predict default risk')

st.subheader('Loan Applicant Details')

age = st.slider('Age', min_value=18, max_value=80, value=30)
income = st.number_input('Annual Income ($)', min_value=0, value=50000)
loan_amount = st.number_input('Loan Amount ($)', min_value=0, value=10000)
credit_score = st.slider('Credit Score', min_value=300, max_value=850, value=600)
months_employed = st.number_input('Months Employed', min_value=0, value=24)
num_credit_lines = st.slider('Number of Credit Lines', min_value=1, max_value=10, value=3)
interest_rate = st.slider('Interest Rate (%)', min_value=1.0, max_value=30.0, value=10.0)
loan_term = st.slider('Loan Term (months)', min_value=12, max_value=60, value=36)
dti_ratio = st.slider('DTI Ratio', min_value=0.0, max_value=1.0, value=0.3)

# Categorical inputs
education = st.selectbox('Education', ['Bachelor\'s', 'Master\'s', 'High School', 'PhD'])
employment_type = st.selectbox('Employment Type', ['Full-time', 'Part-time', 'Self-employed', 'Unemployed'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
loan_purpose = st.selectbox('Loan Purpose', ['Auto', 'Business', 'Education', 'Home', 'Other'])

has_mortgage = st.selectbox('Has Mortgage?', ['Yes', 'No'])
has_dependents = st.selectbox('Has Dependents?', ['Yes', 'No'])
has_cosigner = st.selectbox('Has Co-Signer?', ['Yes', 'No'])


# Predict button
if st.button('Predict Default Risk'):
    
    # Encode binary columns
    has_mortgage_enc = 1 if has_mortgage == 'Yes' else 0
    has_dependents_enc = 1 if has_dependents == 'Yes' else 0
    has_cosigner_enc = 1 if has_cosigner == 'Yes' else 0
    
    # Create input dataframe with all columns
    input_dict = {
        'Age': age, 'Income': income, 'LoanAmount': loan_amount,
        'CreditScore': credit_score, 'MonthsEmployed': months_employed,
        'NumCreditLines': num_credit_lines, 'InterestRate': interest_rate,
        'LoanTerm': loan_term, 'DTIRatio': dti_ratio,
        'HasMortgage': has_mortgage_enc, 'HasDependents': has_dependents_enc,
        'HasCoSigner': has_cosigner_enc,
        
        # OHE Education
        'Education_Bachelor\'s': 1 if education == 'Bachelor\'s' else 0,
        'Education_High School': 1 if education == 'High School' else 0,
        'Education_Master\'s': 1 if education == 'Master\'s' else 0,
        'Education_PhD': 1 if education == 'PhD' else 0,
        
        # OHE Employment
        'EmploymentType_Full-time': 1 if employment_type == 'Full-time' else 0,
        'EmploymentType_Part-time': 1 if employment_type == 'Part-time' else 0,
        'EmploymentType_Self-employed': 1 if employment_type == 'Self-employed' else 0,
        'EmploymentType_Unemployed': 1 if employment_type == 'Unemployed' else 0,
        
        # OHE Marital Status
        'MaritalStatus_Divorced': 1 if marital_status == 'Divorced' else 0,
        'MaritalStatus_Married': 1 if marital_status == 'Married' else 0,
        'MaritalStatus_Single': 1 if marital_status == 'Single' else 0,
        
        # OHE Loan Purpose
        'LoanPurpose_Auto': 1 if loan_purpose == 'Auto' else 0,
        'LoanPurpose_Business': 1 if loan_purpose == 'Business' else 0,
        'LoanPurpose_Education': 1 if loan_purpose == 'Education' else 0,
        'LoanPurpose_Home': 1 if loan_purpose == 'Home' else 0,
        'LoanPurpose_Other': 1 if loan_purpose == 'Other' else 0,
    }
    
    input_df = pd.DataFrame([input_dict])
    
    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    # Show result
    if prediction == 1:
        st.error(f'⚠️ HIGH RISK — Default Probability: {probability:.2%}')
    else:
        st.success(f'✅ LOW RISK — Default Probability: {probability:.2%}')