import streamlit as st
import sqlite3
from home import home_page

# Database connection
conn = sqlite3.connect('newDB.db')
cur = conn.cursor()

# Function to create the user table
def create_table():
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS myTable (
            Username TEXT PRIMARY KEY,
            Password TEXT
        )
        """
    )
    conn.commit()

# Function to add user information to the database
def add_user(username, password):
    cur.execute("INSERT INTO myTable (Username, Password) VALUES (?, ?)", (username, password))
    conn.commit()

# Function to check user credentials
def check_credentials(username, password):
    cur.execute("SELECT * FROM myTable WHERE Username = ? AND Password = ?", (username, password))
    return cur.fetchone()

# Registration form
def registration_form():
    st.title("Register Here")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    confirm_password = st.text_input("Confirm your password", type="password")
    if st.button("Register"):
        if password == confirm_password:
            add_user(username, password)
            st.success("Registration successful! Please log in.")
            st.session_state.page = "login"
            st.experimental_rerun()
        else:
            st.error("Passwords do not match")
            # ****************************************
    st.write("Already have an account?")
    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.experimental_rerun()
           

# Login form
def login_form():
    st.title("Login Here")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    if st.button("Login"):
        user = check_credentials(username, password)
        if user:
            # Redirect One page to Another
            st.success(f"Welcome, {username}!")
            st.session_state.authenticated = True
            st.session_state.page = "home"
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")


def main():
    create_table()
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'page' not in st.session_state:
        st.session_state.page = "register"

    if st.session_state.page == "register":
        registration_form()
    elif st.session_state.page == "login":
        login_form()
    elif st.session_state.page == "home" and st.session_state.authenticated:
        home_page()
    else:
        st.session_state.page = "login"
        login_form()

if __name__ == "__main__":
    main()

conn.close()
