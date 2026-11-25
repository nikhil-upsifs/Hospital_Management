import streamlit as st 
from datetime import date
st.title ("Age Calculator")
birth_date=st.date_input("Enter your date of birth",min_value=date(1900, 1, 1), max_value=date.today())   
current_date = st.date_input("Current date")

if st.button("Calculate Age"):
    today=date.today()
    age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
st.success(f"Your age is: {age} years")