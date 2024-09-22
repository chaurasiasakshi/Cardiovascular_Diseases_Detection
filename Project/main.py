import streamlit as st
from team import team_page  
from contact import contact_page
from Predict import prediction_page
from about import about

# App Configuration
st.set_page_config(page_title="HRIDAM",page_icon="🩺", layout="wide")


st.markdown("""
    <style>
 
    .custom-header {
        font-size: 80px;
        font-weight: bold;
        margin-bottom: 20px;
        color: black; /* Optional: Change header color */
    }
    </style>
    """, unsafe_allow_html=True)


# Navigation button logic with session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def navigate(page):
    st.session_state.page = page

# Button container with navigation
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    if col1.button("Home"):
        navigate("Home")
    if col2.button("About"):
        navigate("About")
    if col3.button("Our Solution"):
        navigate("Our Solution")
    if col4.button("Team"):
        navigate("Team")
    if col5.button("Contact"):
        navigate("Contact")

if st.session_state.page == "Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h1 class="custom-header">Turning member health into Quality success</h1>', unsafe_allow_html=True)
        st.write("""
        Member needs are getting more complex and reimbursements are tightening. We'll help you intelligently identify 
        the right members, deliver personalized clinical intervention, and improve your clinical and quality outcomes.
        """)
        st.button("See Our Plans")

    with col2:
        st.image("0main.jpg", caption="Save Heart", use_column_width=True)
        


    st.markdown("""
<style>
    .stat-card {
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f0f0;
        margin: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stat-card:hover {
        background-color: #e0e0e0;
        transform: scale(1.05);
    }
    .stat-number {
        font-size: 2rem;
        color: #000;
    }
    .stat-description {
        font-size: 1rem;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

    st.header("Statistics")
    with st.container():
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    with stat_col1:
        st.markdown('<div class="stat-card"><div class="stat-number">15 mmHg</div><div class="stat-description">Average reduction in systolic BP</div></div>', unsafe_allow_html=True)
    with stat_col2:
        st.markdown('<div class="stat-card"><div class="stat-number">23%</div><div class="stat-description">Fewer All-Cause 30-Day Readmissions</div></div>', unsafe_allow_html=True)
    with stat_col3:
        st.markdown('<div class="stat-card"><div class="stat-number">20%</div><div class="stat-description">Fewer ED Encounters</div></div>', unsafe_allow_html=True)
    with stat_col4:
        st.markdown('<div class="stat-card"><div class="stat-number">97%</div><div class="stat-description">Average Patient Satisfaction</div></div>', unsafe_allow_html=True)


    with st.container():

        col1, col2, col3 = st.columns(3)

    # Feature 1
    with col1:
        st.image("1.webp", width=250)
        st.subheader("Real-Time Data & Analytics")
        st.write("Intuitive technology enabling proactive care with data-driven interventions and positive member experiences.")

    # Feature 2
    with col2:
        st.image("2.jpg", width=250)
        st.subheader("Clinical Decision Intelligence")
        st.write("Powered by data science, advanced machine learning algorithms deliver unmatched precision.")

    # Feature 3
    with col3:
        st.image("3.jpg", width=250)
        st.subheader("Care Management & Coordination")
        st.write("As an extension of your team, dedicated nurses delivering round-the-clock care to members.")


        

elif st.session_state.page == "About":
    about()
elif st.session_state.page == "Our Solution":
    prediction_page()
elif st.session_state.page == "Team":
    team_page() 
elif st.session_state.page == "Contact":
    contact_page()
    

st.markdown("""
    <style>
    .footer {
        position:relative;
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
