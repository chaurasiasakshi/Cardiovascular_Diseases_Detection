# home.py

import streamlit as st

def home_page():
    st.title("HRIDAI - Cardiovascular Diseases and Detection")
    # st.write("Welcome to the home page!")
    st.markdown("<br><br><h1 class='head1'>Detect your chances of having a cardiovascular diseases because prevention is better than cure!</h1><h3 class='head1'>At <b>HRIDAI </b> We Believe Early Detection is Easy Elmination!</h3>", unsafe_allow_html=True)

    st.markdown(page_bg_img, unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.page = "login"
        st.experimental_rerun()


import base64


st.set_page_config(page_title="HRIDAI", layout="wide")

# Title of the app




# Function to encode local image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your local image
img_file = "ff.jpeg" 

# Get the base64 string of the image
img_base64 = get_base64_of_bin_file(img_file)

# Custom CSS for background image
page_bg_img = f'''
<style>
 div[data-testid="stTabs"] button {{
        font-size: 220px !important;
    }}
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

font-style: italic;
}}
</style>
'''
