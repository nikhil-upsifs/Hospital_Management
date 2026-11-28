import streamlit as st
import os
import mysql.connector
from mysql.connector import errorcode
import datetime as datetime 


st.set_page_config(
    page_title="Hospital Management System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Management System")

st.sidebar.title("🏥 Hospital Management System Menu ")
st.sidebar.caption("Developed by Nikhil")

page = st.sidebar.radio(
    "Menu",
    ["Home", "Patients", "Doctors", "Appointments", "Billing","Search Patient"]
)
#connecting to the database
# Connecting to the database
try:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="Hospital_management"
    )

    cursor = cnx.cursor()
    st.toast("Database Connected Successfully!", icon="✅")

except mysql.connector.Error as err:
    st.error(f"Database Connection Failed: {err}")
    st.stop()

if page == "Patients":
    st.title("Patients Management")
    st.subheader(" ADD NEW PATIENT")
    with st.form("patient_form", clear_on_submit=True):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        disease = st.text_input("Disease")
        submit = st.form_submit_button("Add Patient")

          

        if submit:

            if name and contact and address and disease and blood_group and gender and age:

                try:
                    query = """
                    INSERT INTO Patient
                    (patient_name,blood_Group, patient_age, phone, address, disease_type,gender)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """

                    values = (
                        name,
                        blood_group,
                        age,
                        contact,
                        address,
                        disease,
                        gender
                    )

                    cursor.execute(query, values)
                    cnx.commit()

                    st.success("Patient added successfully! ✅")

                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")

            else:
                st.warning("Please fill all the required fields.")
if page == "Doctors":
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

def choose_Patient():
    query="""SELECT patient_name , disease_type FROM Patient"""
    cursor.execute(query)
    doctors= cursor.fetchall()
    doctor_dict={d[0] for d in doctors}
    selected_name = st.selectbox("Doctor Name",list(doctor_dict.keys()))

    doctor_id = doctor_dict[selected_name]

def choose_Doctor():
    query="""SELECT docter_id ,doctor_name,specialisation FROM doctor"""
    cursor.execute(query)
    return cursor.fetchall()

if page == "Appointments":
    st.title("Appointments Management")
    with st.form("Appointment_form",clear_on_submit=True):
        appointment_date= datetime.datetime.now()
        patient_name=st.selectbox("Patient Name", choose_Patient())
        Doctor_name = st.selectbox("Doctor Name", choose_Doctor())


    