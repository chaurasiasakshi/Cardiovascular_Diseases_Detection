import streamlit as st



# Function for the contact page
def contact_page():
    # st.markdown(page_bg_img, unsafe_allow_html=True)
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
    