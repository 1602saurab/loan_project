import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")
import joblib
import os

# Get the absolute path of the model file
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# Check if the file exists before loading
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
else:
    raise FileNotFoundError(f"❌ Model file not found at: {model_path}")



# Streamlit UI
st.title("Machine Learning Model Predictor")

# Input fields
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)
feature5 = st.number_input("Feature 5", value=0.0)
feature6 = st.number_input("Feature 6", value=0.0)
feature7 = st.number_input("Feature 7", value=0.0)
feature8 = st.number_input("Feature 8", value=0.0)

# Predict button
if st.button("Predict"):
    features = pd.DataFrame([[feature1, feature2, feature3, feature4,feature5, feature6, feature7, feature8]])
    prediction = model.predict(features)
    st.success(f"Predicted Value: {int(prediction[0])}")
