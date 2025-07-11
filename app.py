import streamlit as st
import pickle 
import numpy as np 
import gzip

with gzip.open('rfc_compressed_model.pkl.gz','rb') as f:
    rfc_model = pickle.load(f)

st.title("Loan eligibility Predictor")

Exp= st.number_input("Experience",min_value=0, max_value= 25)
Income = st.number_input("Income",min_value = 0)
Family = st.number_input("Family", min_value=0)
CCAvg = st.number_input("CCAvg", min_value=0)
Mortgage = st.number_input("Mortgage", min_valu=0)
Online = st.selectbox("Online",['Yes','No'])

Online = 1 if Online =='Yes' else 0

if st.button("Check Eligibility"):
    input_data = np.array([Exp, Income, Family, CCAvg, Mortgage, Online])
    prediction = rfc_model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan approved")
    else:
        st.error("Loan denied")
