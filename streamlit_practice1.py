import streamlit as st 
st.title("Hospital Management System")
st.subheader("Welcome to the Hospital Management System")
st.text("This is a simple application to manage hospital data using Streamlit.")
st.write("You can use this application to add, view, and manage patient records, doctor information, and appointment schedules.")
login_option = st.selectbox("Select an option", ["Login", "Register"])
print(login_option)
st.button("Submit")
if login_option == "Login":
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")