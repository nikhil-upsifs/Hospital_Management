import streamlit as st 
from database import connection
import pandas as pd
import mysql.connector

def doctors():
    st.title("Doctors Management ")
    st.subheader(" ADD NEW DOCTOR")
    st.write("Please fill in the details of the doctor below:")
    with st.form("doctor_form", clear_on_submit=True):   
        doctor_name = st.text_input("Doctor Name")
        specialization = st.text_input("Specialization")
        phone = st.text_input("Phone Number")
        address = st.text_area("Address")
        email = st.text_input("Email")
        salary = st.number_input("Salary", min_value=0, step=1000)
        
        submit = st.form_submit_button("Add Doctor")
        if submit:
            if doctor_name and specialization and phone and address and email and salary:
                try:
                    cnx=connection()
                    cursor=cnx.cursor()
                    query = """
                    INSERT INTO Doctor
                    (doctor_name, specialisation, phone, Address, email, salary)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    values = (
                        doctor_name,
                        specialization,
                        phone,
                        address,
                        email,
                        salary
                    )
                    cursor.execute(query, values)
                    cnx.commit()
                    st.success("Doctor added successfully! ✅")
                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")
            else:
                st.warning("Please fill all the required fields.")
