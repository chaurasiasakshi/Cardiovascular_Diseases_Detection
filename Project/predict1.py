import streamlit as st



def prediction_page():


    with st.form(key='heart_disease_form'):
        st.title('Heart Disease Detection Form')

        # User inputs
        age = st.number_input('Age of the person', min_value=1, max_value=120, value=30)
        sex = st.selectbox('Gender of the person', ('Male', 'Female'))
        cp = st.selectbox('Chest Pain type', ('Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'))
        trtbps = st.number_input('Resting blood pressure (in mm Hg)', min_value=80, max_value=200, value=120)
        chol = st.number_input('Cholesterol in mg/dl fetched via BMI sensor', min_value=100, max_value=400, value=200)
        fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', ('No', 'Yes'))
        restecg = st.selectbox('Resting electrocardiographic results', ('Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'))
        thalachh = st.number_input('Maximum heart rate achieved', min_value=60, max_value=220, value=150)
        exng = st.selectbox('Exercise induced angina', ('No', 'Yes'))
        oldpeak = st.number_input('Previous peak', min_value=0.0, max_value=10.0, value=1.0)

        # Form submission button
        submit_button = st.form_submit_button(label='Submit')

        # Handle form submission
        if submit_button:
            st.write("Form Submitted Successfully")