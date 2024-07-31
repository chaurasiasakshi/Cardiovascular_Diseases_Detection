import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Signup Form", layout="wide")

# CSS for the form styling
st.markdown(
    """
    <style>
    .form-container {
        max-width: 500px;
        margin: 0 auto;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .form-title {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }

    .form-field {
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the form container
st.markdown('<div class="form-container">', unsafe_allow_html=True)

# Form title
st.markdown('<div class="form-title">Signup Form</div>', unsafe_allow_html=True)

# Create the form inputs
name = st.text_input("Name", placeholder="Enter your full name", key="name")
email = st.text_input("Email", placeholder="Enter your email address", key="email")
password = st.text_input("Password", placeholder="Enter a password", type="password", key="password")
confirm_password = st.text_input("Confirm Password", placeholder="Re-enter your password", type="password", key="confirm_password")

# Handle the form submission
if st.button("Sign Up"):
    if password == confirm_password:
        st.success("Signup successful! Welcome, {}.".format(name))
    else:
        st.error("Passwords do not match. Please try again.")

# Close the form container
st.markdown('</div>', unsafe_allow_html=True)
