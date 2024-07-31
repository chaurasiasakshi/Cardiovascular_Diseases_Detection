import streamlit as st


st.set_page_config(page_title="HRIDAI", layout="wide")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.ugaoo.com/cdn/shop/articles/shutterstock_223679731.jpg?v=1661873480");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# CSS for the navigation bar
st.markdown(
    """
    <style>
    .navbar {
        background-color: grey;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }

    .navbar a {
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 17px;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }

    .navbar a.active {
        background-color: #4CAF50;
        color: white;
    }

    .navbar .logo {
        font-weight: bold;
        font-size: 20px;
        color: white;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the navigation bar
st.markdown(
    """
    <div class="navbar">
        <a href="#" class="logo">HEART</a>
        <div>
            <a href="#home" class="active">Home</a>
            <a href="#analysis">Analysis</a>
            <a href="#contact">Contact</a>
            <a href="#contact">Admin Login</a>
            <a href="#contact">SignUp</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.title("Heart Diseases Prediction")

st.header("Predict your chance of having a heart disease because prevention is better than cure!")
st.write("This is a sample Streamlit app with a background image.")


# CSS for the form styling
st.markdown(
    """
    <style>
    .form-container {
        max-width: 350px;
        margin: 0 auto;
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
          text-align: center;
        font-size: 24px;
    }

    .form-title {
        text-align: center;
        font-size: 24px;
    }

    .form-field {
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the form
st.markdown('<div class="form-container">Signup Form</div>', unsafe_allow_html=True)
st.markdown('<div class="form-title"></div>', unsafe_allow_html=True)

# Create the form inputs
name = st.text_input("Name", placeholder="Enter your full name", key="name")
email = st.text_input("Email", placeholder="Enter your email address", key="email")
password = st.text_input("Password", placeholder="Enter a password", type="password", key="password")
confirm_password = st.text_input("Confirm Password", placeholder="Re-enter your password", type="password", key="confirm_password")

# Handle the form submission