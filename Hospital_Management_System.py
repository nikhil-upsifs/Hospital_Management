import streamlit as st
import os
import mysql.connector
from mysql.connector import errorcode
import datetime as dt 


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
    ["Home", "Patients", "Doctors", "Appointments", "Billing"]
)
#connecting to the database
# Connecting to the database
try:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
         password=os.getenv("DB_PASSWORD")
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
    with st.form("patient_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        disease = st.text_input("Disease")
        submit = st.form_submit_button("Add Patient")

        if submit:

            if name and contact and address and disease:

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
                        gender,
                        contact,
                        address,
                        disease
                    )

                    cursor.execute(query, values)
                    cnx.commit()

                    st.success("Patient added successfully! ✅")

                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")

            else:
                st.warning("Please fill all the required fields.")
