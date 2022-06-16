# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:33:48 2022

@author: ADMIN
"""

import streamlit as st
import numpy as np
import pickle

emp_perf_model_path1 = open("model.pkl","rb")
emp_perf_model1=pickle.load(emp_perf_model_path1)

def main():
    st.title('Employee Performance Rating Prediction App')
    st.markdown('Just Enter the following details and we will predict the perfermonance rating of your Employee')
    a = st.number_input("Age")
    b = st.number_input("Gender")
    c = st.number_input("Marital status")  
    d = st.number_input("Education")  
    e = st.number_input("Environment Satisfaction")
    f = st.number_input("Job Involvement")
    g = st.number_input("Job level")
    h = st.number_input("Job satisfaction")
    i = st.number_input("Annual income")
    j = st.number_input("Relationship Satisfaction")
    k = st.number_input("Working hrs per Day")
    l = st.number_input("Experience")
    m = st.number_input("Training time")
    n = st.number_input("Work Life Balance")
    o = st.number_input("Behavioural Competence")
    p = st.number_input("On time Delivery")
    q = st.number_input("Ticket Solving Managements")
    r = st.number_input("Project Completion")
    s = st.number_input("Working From Home")
    t = st.number_input("Psycho social indicators")
    u = st.number_input("Over time")
    v = st.number_input("Attendance")
    w = st.number_input("Percent Salary Hike")
    x = st.number_input("Net Connectivity")
    y = st.number_input("Department")
    z = st.number_input("Position")
    submit = st.button('Predict Rating')
    if submit: 
        if a and b and c and d and e and f and g and h and i and j and k and l and m and n and o and p and q and r and s and t and u and v and w and x and y and z:
            values = np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]])
            prediction = emp_perf_model1.predict(values)
            prediction = int(prediction)
            st.write(f"Performance rating of employee is {prediction}") 
            if prediction == 0:
                st.write("Employee's performance is average")
            elif prediction==1:
                st.write("Employee's performance is good")
            else:
                st.write("Employee's performance is low")
        else:
            st.error('Please Enter All the Details')

if __name__ == '__main__':
    main()
