import json 
import streamlit as st 
import os
from datetime import date
from uuid import uuid4


st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰",
    layout="wide"
)
FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f: # show all the expenses in json file
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        st.error("Error loading expenses.")
        return []

def save_expenses(expenses):
    try:
        with open(FILE, "w") as f:
            json.dump(expenses, f, indent=4)
    except OSError:
        st.error("Error saving expenses.")

if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()

# ---------------- SIDEBAR ----------------

st.sidebar.title("💰 Expense Tracker")
st.sidebar.caption("Developed by Nikhil")

page = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Add Expense", "View Expenses"]
)
expenses = st.session_state.expenses

if page == "Dashboard":
    st.title("😸 Dashboard")
    st.write("Welcome to the Expense Tracker! Use the sidebar to navigate through the app.")

    total=sum(float(e["amount"]) for e in expenses)
    today = date.today()
    monthly=sum(
        float(e["amount"])
        for e in expenses
        if e["date"][:7] == today.strftime("%Y-%m")
    )

    col1, col2 = st.columns(2)

    col1.metric("Total Expenses", f"₹{total:,.2f}")
    col2.metric("This Month", f"₹{monthly:,.2f}")

    st.divider()

    st.subheader("Recent Expenses")

    if expenses:
        for e in reversed(expenses[-5:]):
            st.write(
                f"**{e['title']}** | "
                f"{e['category']} | "
                f"₹{float(e['amount']):,.2f} | "
                f"{e['date']}"
            )
    else:
        st.info("No expenses added yet.")


# ---------------- ADD EXPENSE ----------------

elif page == "Add Expense":

    st.title("➕ Add New Expense")

    with st.form("expense_form"):

        title = st.text_input("Expense Name")

        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            step=100.0
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Shopping",
                "Bills",
                "Entertainment",
                "Health",
                "Education",
                "Other"
            ]
        )

        expense_date = st.date_input(
            "Expense Date",
            value=date.today()
        )

        note = st.text_area("Description")

        submit = st.form_submit_button("Add Expense")

        if submit:

            if not title.strip():
                st.error("Enter an expense name.")

            elif amount <= 0:
                st.error("Enter a valid amount.")

            else:

                new_expense = {
                    "id": str(uuid4()),
                    "title": title,
                    "amount": amount,
                    "category": category,
                    "date": expense_date.isoformat(),
                    "note": note
                }

                expenses.append(new_expense)

                save_expenses(expenses)

                st.success("Expense added successfully!")

                st.rerun()


# ---------------- VIEW EXPENSES ----------------

elif page == "View Expenses":

    st.title("📋 All Expenses")

    if not expenses:
        st.info("No expenses available.")

    else:

        search = st.text_input("Search expense")

        filtered = [
            e for e in expenses
            if search.lower() in e["title"].lower()
        ]

        for e in filtered:

            with st.expander(
                f"{e['title']} — ₹{float(e['amount']):,.2f}"
            ):

                st.write("Category:", e["category"])
                st.write("Date:", e["date"])
                st.write("Description:", e["note"])

                if st.button("Delete", key=e["id"]):

                    expenses = [
                        x for x in expenses
                        if x["id"] != e["id"]
                    ]

                    st.session_state.expenses = expenses

                    save_expenses(expenses)

                    st.rerun()
