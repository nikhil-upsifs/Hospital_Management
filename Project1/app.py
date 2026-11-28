import streamlit as st
import mysql.connector
from mysql.connector import errorcode
import datetime as datetime 
from database import connection
import pandas as pd
import patients as pt
import doctor as dc

st.set_page_config(
    page_title="Hospital Management System",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* Main dashboard width */
.stMainBlockContainer {
    max-width: 950px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* Main title */
h1 {
    font-size: 30px !important;
    font-weight: 700 !important;
}

/* Section headings */
h2 {
    font-size: 23px !important;
}

h3 {
    font-size: 19px !important;
}

/* Form container */
[data-testid="stForm"] {
    max-width: 750px;
    padding: 20px;
    border-radius: 12px;
    margin: auto;
}

/* Text input fields */
.stTextInput input {
    height: 38px;
    font-size: 14px;
}

/* Text area */
.stTextArea textarea {
    font-size: 14px;
}

/* Select boxes */
[data-testid="stSelectbox"] {
    font-size: 14px;
}

/* Buttons */
.stButton button,
.stFormSubmitButton button {
    width: auto;
    min-height: 38px;
    padding: 5px 18px;
    font-size: 14px;
    border-radius: 8px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    min-width: 220px;
    max-width: 220px;
}

/* Reduce vertical spacing */
div[data-testid="stVerticalBlock"] {
    gap: 0.8rem;
}

</style>
""", unsafe_allow_html=True)


st.title("🏥 Hospital Management System")

st.sidebar.write("Welcome to Hospital Management System")
st.sidebar.caption("Developed by Nikhil")

page = st.sidebar.radio(
    "Menu",
    ["Home", "Patients", "Doctors", "Appointments", "Billing","Show Patient"]
)

if page == "Home":
    st.title(" Hospital Dashboard")
    

elif page == "Patients":
    pt.Patients_entry()

elif page == "Show Patient":
    pt.show_patients()
    pt.delete_patient()

elif page == "Doctors":
    dc.doctors()

    

    