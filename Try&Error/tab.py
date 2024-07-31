import streamlit as st
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="HRIDAM", layout="wide")

# Title of the app


# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")
    return data

data = load_data()

# Function to encode local image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your local image
img_file = "ff.jpeg"  # Adjust the path as needed

# Get the base64 string of the image
img_base64 = get_base64_of_bin_file(img_file)

# Custom CSS for background image
page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
.head1{{
    text-align: center;    
}}
input{{
width:500px !important;

color: #888;
font-style: italic;
}}
</style>
'''

# Inject CSS with background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Predict", "Analysis", "Register", "Login", "Contact"])





# Content for Tab 1
with tab1:
    st.markdown("<h1 class='head1'>Predict your chance of having a heart disease because prevention is better than cure!</h1>", unsafe_allow_html=True)
    
    # Create buttons in the center
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        check_now = st.button("Check Now")
        analysis = st.button("Analysis")
    with col3:
        st.write("")

    # Handle button clicks
    if check_now:
        st.write("Check Now button clicked")
        # Add your logic for "Check Now" button here

    if analysis:
        st.write("Analysis button clicked")

# Content for Tab 2
with tab2:
    st.header("Heart Disease Prediction")

    # # Sidebar for user inputs
    # st.sidebar.header("User Input Features")

    def user_input_features():
        age = st.slider("Age", 18, 100, 50)
        sex = st.selectbox("Sex", ("Male", "Female"))
        sex = 1 if sex == "Male" else 0
        resting_blood_pressure = st.slider("Resting Blood Pressure", 80, 200, 120)
        cholesterol = st.slider("Cholesterol Level", 100, 400, 200)
        max_heart_rate = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)

        data = {
            "age": age,
            "sex": sex,
            "resting_blood_pressure": resting_blood_pressure,
            "cholesterol": cholesterol,
            "max_heart_rate": max_heart_rate
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Train the Random Forest model
    X = data.drop("target", axis=1)
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    st.write(f"Model Accuracy: {accuracy:.2f}")

    # Predict using the Random Forest model
    prediction = model.predict(input_df)

    # Display the prediction
    st.subheader("Prediction")
    heart_disease = ["No Heart Disease", "Heart Disease"]
    st.write(heart_disease[prediction[0]])


# Content for Tab 3 - Analysis
with tab3:
    st.header("Heart Disease Detection Analysis")

    # Create a sample graph using matplotlib
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    ax.plot(x, y)
    ax.set_title('Sample Heart Disease Detection Graph')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Display the graph in Streamlit
    st.pyplot(fig)

# Content for Tab 4
with tab4:
    st.markdown("<h1 class='head1'>Register Here</h1>", unsafe_allow_html=True)

    # Create a form
    with st.form(key='reg_form'):
        name = st.text_input("Name" , placeholder="Enter your Name" )
        email = st.text_input("Email" , placeholder="Enter your EmailID")
        Password = st.text_input("Password" , placeholder="Enter your Password")
        C_Password = st.text_input("Confirm Password" , placeholder="Confirm Your Password")
        

        # Form submit button
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success(f"Thank you for reaching out! We will get back to you soon, {name}")

# Content for Tab 5
with tab5:
    st.markdown("<h1 class='head1'>Login Here</h1>", unsafe_allow_html=True)
    # Create a form
    with st.form(key='login_form'):
        uname = st.text_input("Username" , placeholder="Enter your Username")
        password = st.text_input("Password", placeholder="Enter your Password")
       
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            st.success(f" Login Successfully , {uname}")

# Content for Tab 6
with tab6:
    st.markdown("<h1 class='head1'>Get In Touch</h1>", unsafe_allow_html=True)   
    # st.write("We would love to hear from you!")

    # Create a form
    with st.form(key='contact_form'):
        name = st.text_input("Name" , placeholder="Enter your Name" )
        email = st.text_input("Email" , placeholder="Enter your EmailID")
        number = st.text_input("Number" , placeholder="Enter your Phone Number")
        message = st.text_input("Message" , placeholder="Enter your Message")
        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            st.success(f"Thank you for reaching out! We will get back to you soon, {name}")


