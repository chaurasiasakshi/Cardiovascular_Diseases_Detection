import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load and preprocess the dataset
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    data = pd.read_csv(url, names=columns)
    data = data.replace('?', np.nan).dropna()
    data = data.astype(float)
    return data

def preprocess_data(data):
    X = data.drop('target', axis=1)
    y = data['target'].apply(lambda x: 1 if x > 0 else 0)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Streamlit app
st.title("Heart Disease Prediction")

st.write("""
### Enter the patient data to predict the likelihood of heart disease
""")

# Sidebar for user input
st.sidebar.header("Patient Data")
def user_input_features():
    age = st.sidebar.slider('Age', 29, 100, 50)
    sex = st.sidebar.selectbox('Sex', [0, 1])
    cp = st.sidebar.selectbox('Chest Pain Type', [0, 1, 2, 3])
    trestbps = st.sidebar.slider('Resting Blood Pressure', 90, 200, 120)
    chol = st.sidebar.slider('Serum Cholesterol', 100, 600, 200)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved', 60, 220, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise', 0.0, 6.0, 1.0)
    slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.sidebar.slider('Number of Major Vessels Colored by Flourosopy', 0, 4, 0)
    thal = st.sidebar.selectbox('Thalassemia', [0, 1, 2, 3])
    
    data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Load and preprocess data
data = load_data()
X_train, X_test, y_train, y_test = preprocess_data(data)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
input_df_scaled = scaler.transform(input_df)

# Train the model
model = train_model(X_train, y_train)

# Prediction
prediction = model.predict(input_df_scaled)
prediction_proba = model.predict_proba(input_df_scaled)

# Display results
st.subheader("Prediction")
heart_disease = np.array(['No Heart Disease', 'Heart Disease'])
st.write(heart_disease[prediction][0])

st.subheader("Prediction Probability")
st.write(f"Probability of Heart Disease: {prediction_proba[0][1]:.2f}")
st.write(f"Probability of No Heart Disease: {prediction_proba[0][0]:.2f}")

# Model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.subheader("Model Accuracy")
st.write(f"Accuracy: {accuracy:.2f}")
