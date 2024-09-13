import streamlit as st
import sqlite3
import base64

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

# Function to create the users table
def create_table(conn):
    try:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')
        conn.commit()
    except Exception as e:
        st.error(f"Error creating table: {e}")

# Function to add a new user to the database
def add_user(conn, username, password):
    try:
        conn.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Function to validate user login
def validate_login(conn, username, password):
    cursor = conn.execute('''
    SELECT * FROM users WHERE username=? AND password=?
    ''', (username, password))
    return cursor.fetchone() is not None

# Function to encode local image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your local image
img_file = "background.jpg"  # Update this to your image path

# Get the base64 string of the image
img_base64 = get_base64_of_bin_file(img_file)

# Custom CSS for background image and nav bar
page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
.navbar {{
    display: flex;
    justify-content: left;
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
}}
.navbar button {{
    margin: 0 10px;
    font-size: 16px;
}}
</style>
'''

# Registration Page
def registration_page(conn):
    st.title("Registration Page")
    with st.form("registration_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button(label="Register")

        if submit_button:
            if password == confirm_password:
                if add_user(conn, username, password):
                    st.success("Registration successful! Please log in.")
                else:
                    st.error("Username already exists. Please choose a different one.")
            else:
                st.error("Passwords do not match!")
    
    st.write("Already have an account?")
    if st.button("Login"):
        st.session_state['page'] = 'login'
        st.experimental_rerun()

# Login Page
def login_page(conn):
    st.title("Login Page")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button(label="Login")

        if login_button:
            if validate_login(conn, username, password):
                st.success("Login successful!")
                st.session_state['authenticated'] = True
                st.session_state['page'] = 'landing'
                st.experimental_rerun()
            else:
                st.error("Invalid username or password!")

    st.write("Don't have an account?")
    if st.button("Create Account"):
        st.session_state['page'] = 'registration'
        st.experimental_rerun()

# Landing Page with Navigation Bar
def landing_page():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    if st.button("Analysis"):
        st.session_state['page'] = 'analysis'
        st.experimental_rerun()
    if st.button("Prediction"):
        st.session_state['page'] = 'prediction'
        st.experimental_rerun()
    if st.button("Contact"):
        st.session_state['page'] = 'contact'
        st.experimental_rerun()
    if st.button("Logout"):
        st.session_state['authenticated'] = False
        st.session_state['page'] = 'login'
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("Welcome to the HRIDAI Landing Page!")


# Sample heart disease data (you can replace this with your real data)
def get_sample_heart_disease_data():
    data = {
        'age': np.random.randint(29, 80, 100),
        'cholesterol': np.random.randint(150, 300, 100),
        'heart_disease': np.random.choice([0, 1], 100, p=[0.6, 0.4])  # 0 = no heart disease, 1 = heart disease
    }
    return pd.DataFrame(data)

# Function for the analysis page
def analysis_page():
    st.title("Analysis of Heart Disease Data")
    
    # Fetch sample data
    df = get_sample_heart_disease_data()
    
    st.write("Here is a summary of the heart disease dataset:")
    st.dataframe(df.head())  # Display first few rows of the dataset

    # Plot: Distribution of Age vs Cholesterol levels
    fig, ax = plt.subplots()
    colors = {0: 'blue', 1: 'red'}
    ax.scatter(df['age'], df['cholesterol'], c=df['heart_disease'].apply(lambda x: colors[x]))
    ax.set_xlabel('Age')
    ax.set_ylabel('Cholesterol Levels')
    ax.set_title('Age vs Cholesterol Levels (Blue = No Heart Disease, Red = Heart Disease)')

    # Display the graph
    st.pyplot(fig)

    if st.button("Back to Home"):
        st.session_state['page'] = 'landing'
        st.experimental_rerun()




# Function for the prediction page
def prediction_page():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.form(key='heart_disease_form'):
        st.title('Heart Disease Detection Form')

        # User inputs
        age = st.number_input('Age of the person', min_value=1, max_value=120, value=30)
        sex = st.selectbox('Gender of the person', ('Male', 'Female'))
        cp = st.selectbox('Chest Pain type', ('Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'))
        trtbps = st.number_input('Resting blood pressure (in mm Hg)', min_value=80, max_value=200, value=120)
        chol = st.number_input('Cholesterol in mg/dl fetched via BMI sensor', min_value=100, max_value=400, value=200)
        fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', ('No', 'Yes'))
        restecg = st.selectbox('Resting electrocardiographic results', ('Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'))
        thalachh = st.number_input('Maximum heart rate achieved', min_value=60, max_value=220, value=150)
        exng = st.selectbox('Exercise induced angina', ('No', 'Yes'))
        oldpeak = st.number_input('Previous peak', min_value=0.0, max_value=10.0, value=1.0)

        # Form submission button
        submit_button = st.form_submit_button(label='Submit')

        # Handle form submission
        if submit_button:
            st.write("Form Submitted Successfully")
            st.write(f"Age: {age}")
            st.write(f"Sex: {sex}")
            st.write(f"Chest Pain Type: {cp}")
            st.write(f"Resting Blood Pressure: {trtbps}")
            st.write(f"Cholesterol: {chol}")
            st.write(f"Fasting Blood Sugar > 120 mg/dl: {fbs}")
            st.write(f"Resting Electrocardiographic Results: {restecg}")
            st.write(f"Maximum Heart Rate Achieved: {thalachh}")
            st.write(f"Exercise Induced Angina: {exng}")
            st.write(f"Previous Peak: {oldpeak}")

    if st.button("Back to Home"):
        st.session_state['page'] = 'landing'
        st.experimental_rerun()




# Function for the contact page
def contact_page():
   
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 class='head1'>Get In Touch With Us</h1>", unsafe_allow_html=True)
    
    st.write("We would love to hear from you!")

    with st.form(key='contact_form'):
        name = st.text_input("Name", placeholder="Enter your Name")
        email = st.text_input("Email", placeholder="Enter your Email ID")
        number = st.text_input("Number", placeholder="Enter your Phone Number")
        message = st.text_area("Message", placeholder="Enter your Message")
        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            st.success(f"Thank you for reaching out! We will get back to you soon, {name}")
    
    if st.button("Back to Home"):
        st.session_state['page'] = 'landing'
        st.experimental_rerun()




# Set up the SQLite database connection
conn = create_connection()
create_table(conn)

# Setting up page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'registration'
    st.session_state['authenticated'] = False

# Navigation logic
if st.session_state['page'] == 'registration':
    registration_page(conn)
elif st.session_state['page'] == 'login':
    login_page(conn)
elif st.session_state['page'] == 'landing' and st.session_state.get('authenticated', False):
    landing_page()
elif st.session_state['page'] == 'analysis':
    analysis_page()
elif st.session_state['page'] == 'prediction':
    prediction_page()
elif st.session_state['page'] == 'contact':
    contact_page()
