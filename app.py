import streamlit as st

# Title of the dashboard
st.title("Cardiovascular Diseases Detection Dashboard")

from PIL import Image

# Load and display an image
image = Image.open('pc.webp')
st.image(image, caption='', use_column_width=True)


# Sidebar for user inputs
st.sidebar.header("User Input Features")

# User inputs
age = st.sidebar.slider("Age", 18, 100, 50)
sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
resting_blood_pressure = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.sidebar.slider("Cholesterol Level", 100, 400, 200)
max_heart_rate = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)

# Display the user inputs
st.subheader("User Input Summary")
st.write(f"**Age:** {age}")
st.write(f"**Sex:** {sex}")
st.write(f"**Resting Blood Pressure:** {resting_blood_pressure} mm Hg")
st.write(f"**Cholesterol Level:** {cholesterol} mg/dL")
st.write(f"**Maximum Heart Rate Achieved:** {max_heart_rate} bpm")
