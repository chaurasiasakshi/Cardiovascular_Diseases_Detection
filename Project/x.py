import streamlit as st

# Inject custom CSS for the navbar and images
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .navbar button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }
    .navbar button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .image-row {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


def display_home_page():
    st.title("HRIDAM")

    col1, col2 = st.columns([2, 1]) 
    
    with col1:
        st.subheader("About This Project")
        st.write("""
        This is a brief introduction to the project. The project aims to achieve something meaningful 
        by utilizing advanced techniques in web development and AI. 
        It involves multiple modules that work together to produce great results.
        Here, we discuss:
        - The problem statement
        - The solution
        - The tools used
        - The expected outcome
        
        Feel free to explore more details by navigating through other sections!
        """)
    
    # Right side: Image
    with col2:
        st.image("0main.jpg", caption="Welcome Image", use_column_width=True)

    
    # Small horizontal box with 3 images
    st.markdown('<div class="image-row">', unsafe_allow_html=True)
    
    # Create columns with custom background colors using Streamlit and CSS
    col1, col2, col3 = st.columns(3)

    # First column with a light blue background
    with col1:
        st.markdown("""
            <div style="background-color: #E3F2FD; padding: 10px; border-radius: 10px;">
        """, unsafe_allow_html=True)
        st.image("1.webp", caption="Real-Time Data & Analytics", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Second column with a light green background
    with col2:
        st.markdown("""
            <div style="background-color: #E8F5E9; padding: 10px; border-radius: 10px;">
        """, unsafe_allow_html=True)
        st.image("2.jpg", caption="Clinical Decision Intelligence", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Third column with a light grey background and slightly bigger image
    with col3:
        st.markdown("""
            <div style="background-color: #F5F5F5; padding: 10px; border-radius: 10px;">
        """, unsafe_allow_html=True)
        st.image("3.jpg", caption="Care Management", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Function to display other pages
def display_page(page):
    if page == "Home":
        display_home_page()
    elif page == "About":
        st.title("About Us")
        st.write("Here you can describe your project or yourself.")
    elif page == "Projects":
        st.title("Our Projects")
        st.write("Showcase your projects here.")
    elif page == "Contact":
        st.title("Contact Us")
        st.write("Display your contact information here.")

# Set initial page to Home
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Create a horizontal navbar using buttons with custom styling
st.markdown('<div class="navbar">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Home"):
        st.session_state.current_page = "Home"
with col2:
    if st.button("About"):
        st.session_state.current_page = "About"
with col3:
    if st.button("Projects"):
        st.session_state.current_page = "Projects"
with col4:
    if st.button("Contact"):
        st.session_state.current_page = "Contact"

st.markdown('</div>', unsafe_allow_html=True)

# Display the current page
display_page(st.session_state.current_page)

# Add a centered footer at the bottom of the page
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        text-decoration: none;
        color: #000;
        font-weight: bold;
        padding-left: 10px;
    }
    </style>
    <div class="footer">
        © 2024 All rights reserved | <a href="#">Terms</a> | Hridam
    </div>
    """, unsafe_allow_html=True)
