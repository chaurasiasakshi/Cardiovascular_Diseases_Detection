import streamlit as st
from joblib import load

def load_model():
    # Load your model from the joblib file
    model = load('rfp')
    return model

def prediction_page():
    # Load the model
    model = load_model()

    with st.form(key='heart_disease_form'):
        st.title('Heart Disease Detection Form')

        # User inputs
        age = st.number_input('Age of the person', min_value=1, max_value=120, value=30)
        sex = st.selectbox('Gender of the person', ('Male', 'Female'))
        cp = st.selectbox('Chest Pain type', ('Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'))
        trestbps = st.number_input('Resting blood pressure (in mm Hg)', min_value=80, max_value=200, value=120)
        chol = st.number_input('Cholesterol in mg/dl fetched via BMI sensor', min_value=100, max_value=400, value=200)
        fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', ('No', 'Yes'))
        restecg = st.selectbox('Resting electrocardiographic results', ('Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'))
        thalach = st.number_input('Maximum heart rate achieved', min_value=60, max_value=220, value=150)
        exang = st.selectbox('Exercise induced angina', ('No', 'Yes'))
        oldpeak = st.number_input('Previous peak', min_value=0.0, max_value=10.0, value=1.0)
        slope = st.selectbox('Slope of the peak exercise ST segment', ('Up sloping', 'Flat', 'Down sloping'))
        ca = st.number_input('Number of major vessels (0-3)', min_value=0, max_value=3, value=0)
        thal = st.selectbox('Thalassemia', ('Normal', 'Fixed defect', 'Reversible defect'))

        # Form submission button
        submit_button = st.form_submit_button(label='Submit')

        # Handle form submission
        if submit_button:
            # Prepare the input data for prediction
            input_data = [[
                age,
                1 if sex == 'Male' else 0,  # Encode gender
                cp,
                trestbps,
                chol,
                1 if fbs == 'Yes' else 0,  # Encode fasting blood sugar
                restecg,
                thalach,
                1 if exang == 'Yes' else 0,  # Encode exercise induced angina
                oldpeak,
                slope,
                ca,
                thal
            ]]

            # Make prediction
            prediction = model.predict(input_data)

            # Display the prediction result
            st.write("Prediction: ", "Heart Disease" if prediction[0] == 1 else "No Heart Disease")

