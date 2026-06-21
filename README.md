# 🏦 Loan Default Prediction

An end-to-end machine learning project to predict loan defaults using XGBoost, with an interactive Power BI dashboard and Streamlit web app.

## 🔗 Live Demo
[Click here to try the app](https://loan-default-prediction-z534fmjeuakl3x6augqtyl.streamlit.app/)

## 📋 Project Overview
Banks lose significant money when borrowers default on loans. This project builds a machine learning model to predict the probability of loan default before approving a loan — helping banks make smarter lending decisions.

## 🛠️ Tech Stack
- **Python** — Data analysis & ML
- **XGBoost** — Classification model
- **SHAP** — Model explainability
- **Power BI** — Interactive dashboard
- **Streamlit** — Web app deployment
- **GitHub** — Version control

## 📊 Dataset
- Source: [Kaggle — Loan Default Prediction](https://www.kaggle.com/datasets/nikhil1e9/loan-default)
- 255,347 rows × 18 columns
- Target variable: Default (0 = No, 1 = Yes)
- Class imbalance: 88.4% non-default vs 11.6% default

## 🔄 Project Pipeline
1. Problem Understanding — Binary classification, ROC-AUC & Recall as metrics
2. Data Loading & First Look — Shape, dtypes, missing values
3. Exploratory Data Analysis — Countplot, histograms, boxplots, bar charts, heatmap
4. Data Cleaning & Encoding — Label Encoding + One Hot Encoding
5. Feature Engineering — DTIRatio already present, kept all features
6. Class Imbalance — SMOTE on training data + scale_pos_weight=7.5
7. Model Selection — XGBoost chosen over Logistic Regression, Random Forest
8. Model Training & Evaluation — ROC-AUC: 0.75, Recall: 0.71
9. Model Explainability — SHAP values, top features: Age, InterestRate, Income
10. Power BI Dashboard — KPI cards, default rate by category, risk distribution
11. Streamlit Deployment — Live web app deployed on Streamlit Community Cloud

## 📈 Model Results
| Metric | Value |
|--------|-------|
| ROC-AUC | 0.75 |
| Recall (Defaulters) | 0.71 |
| Precision (Defaulters) | 0.21 |
| False Negatives | 1,699 |

## 🔍 Key Insights
- Unemployed borrowers have highest default rate (13.5%)
- High School educated borrowers default more than PhD holders
- Higher Age and Income reduce default risk
- High Interest Rate increases default risk significantly
- Dataset is synthetically generated — confirmed by uniform distribution

## 🚀 How to Run Locally
1. Clone the repository
   git clone https://github.com/Rohith80231/loan-default-prediction.git

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

## 📁 Project Structure
loan-default-prediction/
├── app.py                  # Streamlit web app
├── loan_model.pkl          # Trained XGBoost model
├── loan_predictions.csv    # Model predictions
├── Loan_default.csv        # Original dataset
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

## 💡 Limitations
- Dataset is synthetically generated with uniform distribution
- Low precision (0.21) means model overestimates default risk
- Real world performance may vary with actual bank data

## 👤
