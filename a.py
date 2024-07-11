import streamlit as st

# Set background color
st.markdown(
    """
    <style>
    .main {
        background-color: lightgreen;  
    }
    h1{
    color:red;}
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Heart Disease Prediction System")

# Create a form
with st.form(key='my_form'):
    name = st.text_input('Name')
    password = st.number_input('Password', min_value=0)
    email = st.text_input('Email')

    submit_button = st.form_submit_button(label='Log-In')

# Handle form submission
if submit_button:
    st.write(f'Name: {name}')
    st.write(f'Password: {password}')
    st.write(f'Email: {email}')
