#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:39:57 2024

@author: benjamindavidson
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# loading saved models 

diabetes_model = pickle.load(open('diabetes_model.sav',"rb"))

heart_disease_model = pickle.load(open('heart_disease_model.sav',"rb"))

#sidebar for navigation 

with st.sidebar:
    selected = option_menu("Disease Prediction",
                           ["Diabetes Prediction",
                            "Heart Disease Prediction"],
                            
                           icons = ["activity","heart"],
                           
                           default_index = 0)
    
# diabetes page 

if (selected == "Diabetes Prediction"):
    
    #page name 
    st.title("Diabetes Prediction Using ML")

    #data input from user 

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    
    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness at Tricep")
    
    with col2:
        Insulin = st.text_input("Insulin Level")
    
    with col3:
        BMI = st.text_input("BMI") 
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    
    with col2:
        Age = st.text_input("Age of Person")
    

# code for prediction
    diab_diagnosis = ""

#create button for prediction
    if st.button("Click for Diabetes Prediction"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0] == 1):
            diab_diagnosis = "The Person is Likely Diabetic"
        else:
                diab_diagnosis = "The Person is Likely Non-Diabetic"
        
        st.success(diab_diagnosis)

    
    
    
# heart disease page 
if (selected == "Heart Disease Prediction"):
    
    #page name 
    st.title("Heart Disease Prediction Using ML")
    
    # input data from user 
 
    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.text_input("Persons Sex")
    
    with col2:
        cp = st.text_input("Chest pain Catagory")

    with col3:
        trestbps = st.text_input("Resting Blood Pressure")
    
    with col1:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    
    with col2:
        fbs = st.text_input("Fastling Blood Sugar > 120 mm/dL")
    
    with col3:
        restecg = st.text_input("Resting ECG results") 
    
    with col1:
        thalach = st.text_input("Max Heart Rate Acheived ")
    
    with col2:
        exang = st.text_input("Exercise Induced Angina")

    with col3:
        oldpeak = st.text_input("ST Depression Caused by Exercise")
    
    with col1:
        slope = st.text_input("Slope of Peak exercise ST Segment")
    
    with col2:
        ca = st.text_input("Major Vessels colored by Flourosopy")
    
    with col3:
        thal = st.text_input("thal: 0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect")
    
    # code for prediction
    hd_diagnosis = ""

    #create button for prediction
    if st.button("Click for Heart Disease Prediction"):
        hd_prediction = heart_disease_model.predict([[sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
        if (hd_prediction[0] == 1):
            hd_diagnosis = "The Person Likely Has Heart Disease"
        else:
            hd_diagnosis = "The Person Likely Does Not Have Heart Disease"
        
        st.success(hd_diagnosis)
    

    
