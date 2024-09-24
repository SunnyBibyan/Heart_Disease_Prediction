import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the model
rf_model = joblib.load('heart_disease_model.pkl')

# Title of the app
st.title("❤️ Heart Disease Prediction App")

st.markdown("""
Enter your health details below, and the model will predict the likelihood of having heart disease.
""")
#columns for input fields
col1, col2, col3 = st.columns(3)
# Input fields
with col1:
    age = st.number_input('Age', min_value=1, max_value=120, value=25)

with col2:
    sex = st.selectbox('Sex', ('Male', 'Female'))

with col3:
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], help="0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic")

with col1:
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=200, value=120)

with col2:
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0, max_value=600, value=150)

with col3:
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])

with col1:
    restecg = st.selectbox('Resting ECG Results', [0, 1, 2])

with col2:
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, value=150)

with col3:
    exang = st.selectbox('Exercise Induced Angina', [0, 1])

with col1:
    oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=0.0)

with col2:
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])

with col3:
    ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3])

with col1:
    thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

# Prediction button
if st.button("🔍 Predict"):
    try:
        # Input validation (optional)
        if age < 1 or age > 120:
            st.warning("Please enter a valid age between 1 and 120.")
        else:
            # Prepare input data
            input_data = pd.DataFrame([[age, 1 if sex == 'Male' else 0, cp, trestbps, chol, fbs, restecg,
                                        thalach, exang, oldpeak, slope, ca, thal]],
                                      columns=['age', 'sex', 'cp', 'trestbps', 'chol',
                                               'fbs', 'restecg', 'thalach', 'exang',
                                               'oldpeak', 'slope', 'ca', 'thal'])
            
            # Make prediction
            prediction = rf_model.predict(input_data)[0]
            prediction_proba = rf_model.predict_proba(input_data)[0][prediction]
            
            # Display result
            if prediction == 1:
                st.error(f"The model predicts that you **may have heart disease** with a probability of **{prediction_proba:.2%}**.")
                st.info("**Recommendation:** It's advisable to consult with a healthcare professional for a comprehensive evaluation.")
            else:
                st.success(f"The model predicts that you are **unlikely to have heart disease** with a probability of **{prediction_proba:.2%}**.")
                st.info("**Recommendation:** Maintain a healthy lifestyle to keep your heart disease risk low.")
            
            # Display probability chart
            fig, ax = plt.subplots()
            categories = ['No Heart Disease', 'Heart Disease']
            probabilities = rf_model.predict_proba(input_data)[0]
            colors = ['green', 'red']
            ax.bar(categories, probabilities, color=colors)
            ax.set_ylim(0, 1)
            ax.set_ylabel('Probability')
            ax.set_title('Heart Disease Prediction Probability')
            for index, value in enumerate(probabilities):
                ax.text(index, value + 0.02, f"{value:.2%}", ha='center')
            st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
