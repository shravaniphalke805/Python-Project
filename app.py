import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------

try:
    model = joblib.load("loan_approval_model.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()
# ---------------------------
# Custom CSS
# ---------------------------

st.markdown("""
<style>

.main{
background:#fafafa;
}

h1,h2,h3{
color:#1f2937;
}

.metric{
background:white;
padding:15px;
border-radius:10px;
text-align:center;
box-shadow:0px 0px 5px lightgray;
}

.predict{
width:100%;
background:#0066ff;
color:white;
padding:10px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------

with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png",width=150)

    st.header("Project Details")

    st.info("""
**Project:** Loan Approval Prediction

**Algorithm:** Logistic Regression

**Frontend:** Streamlit

**Developer:** Your Name
""")

# ---------------------------
# Title
# ---------------------------

st.title("🏦 Loan Approval Prediction System")

st.subheader("Predict Whether a Loan Will Be Approved Using Machine Learning")

# ---------------------------
# Top Cards
# ---------------------------

c1,c2,c3=st.columns(3)

with c1:
    st.metric("Dataset","1000 Records")

with c2:
    st.metric("Model","Logistic Regression")

with c3:
    st.metric("Accuracy","93%")

st.divider()

# ---------------------------
# Input Layout
# ---------------------------

left,right=st.columns(2)

with left:

    st.header("📋 Applicant Information")

    income=st.number_input("Income",0,1000000,50000)

    credit_score=st.number_input("Credit Score",300,900,700)

    loan_amount=st.number_input("Loan Amount",0,1000000,100000)

    years_employed=st.number_input("Years Employed",0,50,5)

with right:

    st.header("✨ Additional Details")

    points=st.number_input("Points",0,100,60)

    city=st.text_input("City")

    name=st.text_input("Applicant Name")

st.write("")

# ---------------------------
# Prediction
# ---------------------------

if st.button("Predict Loan Approval",use_container_width=True):

    input_df=pd.DataFrame({

        "name":[name],
        "city":[city],
        "income":[income],
        "credit_score":[credit_score],
        "loan_amount":[loan_amount],
        "years_employed":[years_employed],
        "points":[points]

    })

    input_df=pd.get_dummies(input_df)

    input_df=input_df.reindex(columns=columns,fill_value=0)

    input_scaled=scaler.transform(input_df)

    prediction=model.predict(input_scaled)

    st.divider()

    if prediction[0]==1:

        st.success("🎉 Congratulations! Loan Approved")

    else:

        st.error("❌ Sorry! Loan Rejected")
        