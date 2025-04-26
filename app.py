import streamlit as st
import joblib
import numpy as np

# Load model and features
model = joblib.load('models/diabetes_model_rf.pkl')
features = joblib.load('models/feature_names.pkl')

# Symptom descriptions
symptom_explanations = {
    "polyuria": "Polyuria (frequent urination)",
    "polydipsia": "Polydipsia (excessive thirst)",
    "sudden_weight_loss": "Sudden Weight Loss (unexplained rapid weight loss)",
    "weakness": "Weakness (unusual tiredness)",
    "polyphagia": "Polyphagia (excessive hunger)",
    "genital_thrush": "Genital Thrush (yeast infection)",
    "visual_blurring": "Visual Blurring (blurry vision)",
    "itching": "Itching (especially around private parts)",
    "irritability": "Irritability (mood changes)",
    "delayed_healing": "Delayed Healing (slow wound healing)",
    "partial_paresis": "Partial Paresis (muscle weakness)",
    "muscle_stiffness": "Muscle Stiffness (difficulty moving muscles)",
    "alopecia": "Alopecia (hair loss)",
    "obesity": "Obesity (severely overweight)"
}

st.title("🩺 Diabetes Risk Prediction from Early Symptoms")
st.write("Please answer the questions below based on your symptoms:")

user_input = []
symptom_selected = []

for feature in features:
    if feature == "age":
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        user_input.append(age)
    elif feature == "gender":
        gender = st.radio("Gender", ["Male", "Female"])
        user_input.append(1 if gender == "Male" else 0)
    else:
        label = symptom_explanations.get(feature, feature.replace('_', ' ').title())
        val = st.radio(f"{label}?", ["Yes", "No"], key=feature)
        user_input.append(1 if val == "Yes" else 0)
        if val == "Yes":
            symptom_selected.append(label)

# Predict
if st.button("Predict"):
    pred = model.predict([np.array(user_input)])
    
    if pred[0] == 1:
        if len(symptom_selected) == 1:
            st.warning(f"⚠️ High Risk detected based on one key symptom: **{symptom_selected[0]}**.\nWe recommend consulting a healthcare provider for further evaluation.")
        elif len(symptom_selected) > 1:
            st.error(f"⚠️ High Risk detected based on multiple symptoms: {', '.join(symptom_selected)}.\nImmediate medical attention is recommended.")
        else:
            st.error("⚠️ High Risk: Model prediction indicates diabetes risk based on demographic factors (e.g., age, gender).")
    else:
        st.success("✅ Low Risk: You are unlikely to have diabetes based on the provided information.")
