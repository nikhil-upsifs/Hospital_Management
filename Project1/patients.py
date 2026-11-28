
from database import connection
import streamlit as st
import mysql.connector
import pandas as pd


def Patients_entry():
    st.title("Patients Management")
    st.subheader("ADD NEW PATIENT")
    with st.form("patient_form", clear_on_submit=True):

        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        blood_group = st.selectbox(
            "Blood Group",
            ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        )
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        disease = st.text_input("Disease")
        submit = st.form_submit_button("Add Patient")
        if submit:
            if name and contact and address and disease:
                try:
                    cnx = connection()
                    cursor = cnx.cursor()
                    query = """
                    INSERT INTO Patient
                    (patient_name, blood_Group, patient_age,
                    phone, address, disease_type, gender)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    values = (
                        name, blood_group, age,
                        contact, address, disease, gender
                    )
                    cursor.execute(query, values)
                    cnx.commit()
                    st.success("Patient added successfully!")
                    cursor.close()
                    cnx.close()
                except mysql.connector.Error as err:
                    st.error(f"Database Error: {err}")
            else:
                st.warning("Please fill all required fields.")


# IMPORTANT: This function must be outside patients()

def show_patients():
    st.subheader("ALL REGISTERED PATIENTS")
    try:
        cnx = connection()
        df = pd.read_sql("SELECT * FROM Patient", cnx)
        st.dataframe(df, use_container_width=True)
        cnx.close()
    except Exception as e:
        st.error(f"Error: {e}")


def delete_patient():

    st.title("🗑️ Delete Patient Records")
    st.write("Enter the patient's name to find their records.")

    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )
    if st.button("🔍 Search Patient"):
        if patient_name.strip():
            try:
                cnx = connection()
                cursor = cnx.cursor(dictionary=True)

                query = """
                SELECT * FROM Patient
                WHERE patient_name LIKE %s
                """

                cursor.execute(
                    query,
                    (f"%{patient_name.strip()}%",)
                )

                patients = cursor.fetchall()

                cursor.close()
                cnx.close()

                if patients:
                    st.session_state["delete_results"] = patients
                    st.success(f"{len(patients)} matching record(s) found!")

                else:
                    st.session_state["delete_results"] = []
                    st.warning("No patient found!")

            except mysql.connector.Error as err:
                st.error(f"Database Error: {err}")

        else:
            st.warning("Please enter a patient name.")

    # Display matching patients
    patients = st.session_state.get("delete_results", [])

    if patients:

        st.subheader("Matching Patient Records")
        for patient in patients:
            with st.container(border=True):
                st.write(
                    f"**Patient Name:** {patient['patient_name']}"
                )
                st.write(
                    f"**Age:** {patient['patient_age']}"
                )
                st.write(
                    f"**Blood Group:** {patient['blood_Group']}"
                )
                st.write(
                    f"**Contact:** {patient['phone']}"
                )
                patient_id = patient["patient_id"]
                confirm = st.checkbox(
                    f"Confirm deletion of {patient['patient_name']} "
                    f"(ID: {patient_id})",
                    key=f"confirm_{patient_id}"
                )

                if st.button(
                    "🗑️ Delete Record",
                    key=f"delete_{patient_id}",
                    type="primary"
                ):
                    if confirm:

                        try:
                            cnx = connection()
                            cursor = cnx.cursor()

                            query = """
                            DELETE FROM Patient
                            WHERE patient_id = %s
                            """
                            cursor.execute(query, (patient_id,))
                            cnx.commit()

                            cursor.close()
                            cnx.close()

                            st.success("Patient deleted successfully!")

                            st.session_state["delete_results"] = []
                            st.rerun()

                        except mysql.connector.Error as err:
                            st.error(f"Database Error: {err}")
                    else:
                        st.warning("Please confirm deletion first.")
