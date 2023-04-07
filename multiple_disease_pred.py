# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:28:31 2023

@author: 91801
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

heart_disease_model = pickle.load(open('C:/Users/91801/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav', 'rb'))
# similarly load kidney disease model ...


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           
                           ['Heart Disease Prediction',
                            'Kidney Disease Prediction'],
                           
                           icons = ['heart', 'activity'],
                           
                           default_index = 0)


# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Using Machine Learning')
    
    male = st.number_input('Gender (1 : Male; 0 : Female)')
    age = st.number_input('Age')
    education = st.number_input('Education status (1 : Illiterate; 2 : High School; 3 : Undergraduate; 4 : Graduate)')
    currentSmoker = st.number_input('Smoking status (1 : Yes; 0 : No)')
    cigsPerDay = st.number_input('Cigarettes per day')
    BPMeds = st.number_input('BP Meds (1 : Yes; 0 : No)')
    prevalentStroke = st.number_input('Prevalent Stroke (1 : Yes; 0 : No)')
    prevalentHyp = st.number_input('Prevalent Hypertension (1 : Yes; 0 : No)')
    diabetes = st.number_input('Diabetes (1 : Yes; 0 : No)')
    totChol = st.number_input('Total Cholesterol')
    sysBP = st.number_input('Systolic blood pressure')
    diaBP = st.number_input('Diastolic blood pressure')
    BMI = st.number_input('Body Mass Index (BMI)')
    heartRate = st.number_input('Heart Rate')
    glucose = st.number_input('Glucose')
    
    
    # code for prediction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        
        heart_disease_prediction = heart_disease_model.predict([[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])
        
        if (heart_disease_prediction[0] == 1):
            heart_diagnosis = 'The person has a heart disease'
        
        else:
            heart_diagnosis = 'The person does not have a heart disease'
   
    st.success(heart_diagnosis)

if(selected == 'Kidney Disease Prediction'):
    
    # page title
    st.title('Kidney Disease Prediction Using Machine Learning')
    
    

