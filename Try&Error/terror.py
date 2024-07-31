import streamlit as st

st.set_page_config(page_title="Heart Diseases Prediction", layout="wide")

# Title of the app
st.title("Heart Diseases Prediction")

# Create tabs
tabs = st.selectbox("Choose a tab", ["Contact"])
st.markdown(f"""
<style>

.p1{{
width:500px !important;
background-color:lightblue;
color: #888;
font-style: italic;
}}
            .Span{{
            margin:10px;
            width:100%;
            color:purple;
            }}
</style>
""" , unsafe_allow_html=True)
#  st.markdown("<h1 class='head1'>Get In Touch</h1>", unsafe_allow_html=True)


if tabs == "Contact":
    st.markdown("<h1 class='head1'>Get In Touch</h1>", unsafe_allow_html=True)
    st.write("We would love to hear from you!")
    st.markdown("<div class='p1' >  <input class='Span' type='text' placeholder='enter your name'><br> <input class='Span' type='email' placeholder='enter your email'></div>", unsafe_allow_html=True)
    # st.markdown("<span class='Span' > this a span element")
    # st.markdown("</p>")


    # Create a form
    with st.form(key='contact_form'):
        name = st.text_input("Name", placeholder="Enter your Name")
        email = st.text_input("Email", placeholder="Enter your EmailID")
        number = st.text_input("Number", placeholder="Enter your Phone Number")
        message = st.text_area("Message", placeholder="Enter your Message")
        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            st.success(f"Thank you for reaching out! We will get back to you soon, {name}")

