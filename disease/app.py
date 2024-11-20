#importing the libraries
import pandas as pd
import pickle
import streamlit as st
from st.sidebar.selectbox import option_menu 

option = st.sidebar.selectbox(
    'Choose an option',
    ['disease\breast_cancer_model.pkl', 'disease\diabetes_model.pkl', 'disease\heart_disease_model.pkl']
)

st.write('You selected:', option)

#loading the models
diabetes = pickle.load(open("diabetes_model.pkl", "rb"))

heart_disease = pickle.load(open("heart_disease_model.pkl", "rb"))

parkinsons_disease = pickle.load(open("parkinsons_model.pkl", "rb"))

breast_cancer = pickle.load(open("breast_cancer_model.pkl", "rb"))

lung_cancer = pickle.load(open("lung_cancer_model.pkl", "rb"))