#https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import pickle


model = pickle.load(open('model.pkl', 'rb'))
MMS = pickle.load(open('MMS.pkl', 'rb'))

html_temp=""" <div style="background-color:Blue;padding:2px"> """

def run():
    img1 = Image.open('CreditCard-Visa_MasterCard.jpg')
    img1 = img1.resize((746, 300))
    st.image(img1, use_column_width=False)
    st.title("Credit Card Approval Prediction")

    st.markdown(html_temp, unsafe_allow_html=True)

# User Inputs
    Gender = st.radio("Gender: ", ['Male', 'Female'])
    if Gender =='Male':
        Gender=1
    else:
        Gender=0
    
    Car = st.radio("Car: ", ['Yes', 'No'])
    if Car =='Yes':
        Car=1
    else:
        Car=0

    Property = st.radio("Property: ", ['Yes', 'No'])
    if Property =='Yes':
        Property=1
    else:
        Property=0
    
    Children = st.number_input("No of Children:", step = 1)
    
    Income = st.number_input("Annual Income:", step = 1)
    
    Income_list = ['Commercial associate', 'Pensioner', 'State servant', 'Student','Working']
    Income_Type = st.selectbox("Type of Income: ", Income_list)
    Income_Type = Income_list.index(Income_Type)
    
    Education_list = ['Academic degree', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Secondary / secondary special']
    Education_Type = st.selectbox("Type of Education: ", Education_list)
    Education_Type = Education_list.index(Education_Type)
    
    Family_list = ['Civil marriage', 'Married', 'Separated', 'Single / not married', 'Widow']
    Family_Status = st.selectbox("Family Status: ", Family_list)
    Family_Status = Family_list.index(Family_Status)
    
    Housing_list = ['Co-op apartment', 'House / apartment', 'Municipal apartment', 'Rented apartment', 'With parents']
    Housing_Type = st.selectbox("Housing Type: ", Housing_list)
    Housing_Type = Housing_list.index(Housing_Type)
    
    Age = st.number_input("Age (Years):", step = 1)
    
    Employed = st.number_input("No of Years Employed:", step = 1)
        
    Family_Members = st.number_input("No of Family Members:", step = 1)

    st.markdown(html_temp, unsafe_allow_html=True)
# Model Prediction
    if st.button("Submit"):
        features = np.array([[Gender, Car, Property, Children, Income, Income_Type, Education_Type, Family_Status, Housing_Type, Age, Employed, Family_Members]])
        final_features = MMS.transform(features)
        prediction = model.predict(final_features)
        
        if prediction==0:
            st.success("Your Credit Card application will get Approved")
        else:
            st.error("Your Credit Card application will get Rejected")      
run()
