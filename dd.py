import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")
    return data

data = load_data()

# Title of the app
st.title("Heart Disease Prediction")

# Display the dataset
if st.checkbox("Show raw data"):
    st.write(data)

# Sidebar for user inputs
st.sidebar.header("User Input Features")

def user_input_features():
    age = st.sidebar.slider("Age", 18, 100, 50)
    sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
    sex = 1 if sex == "Male" else 0
    resting_blood_pressure = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
    cholesterol = st.sidebar.slider("Cholesterol Level", 100, 400, 200)
    max_heart_rate = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)
    
    data = {
        "age": age,
        "sex": sex,
        "resting_blood_pressure": resting_blood_pressure,
        "cholesterol": cholesterol,
        "max_heart_rate": max_heart_rate
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Train the Random Forest model
X = data.drop("target", axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.write(f"Model Accuracy: {accuracy:.2f}")

# Predict using the Random Forest model
prediction = model.predict(input_df)

# Display the prediction
st.subheader("Prediction")
heart_disease = ["No Heart Disease", "Heart Disease"]
st.write(heart_disease[prediction[0]])
