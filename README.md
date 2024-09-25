# Heart Disease Prediction Using Ensemble Methods 🫀

## Overview
This project applies **ensemble methods** such as **Random Forest** (Bagging) and **Gradient Boosting** (Boosting) to predict the likelihood of heart disease based on clinical features. The project is designed to offer an easy-to-use web interface using **Streamlit**, allowing users to input clinical data and receive predictions.

## Key Features
- **Data Sources**: The dataset includes clinical information like age, sex, cholesterol levels, and more to predict heart disease.
- **Ensemble Models**: Utilizes **Random Forest**, **Gradient Boosting**, and **XGBoost** for prediction.
- **Evaluation Metrics**: Includes precision, recall, F1-score, and ROC-AUC for model evaluation.
- **Streamlit Application**: A web-based interface where users can input their details and get real-time predictions.

## Tools & Technologies
- **Python**: For model building and data processing.
- **Scikit-learn**: Used for machine learning algorithms and metrics.
- **XGBoost**: For optimized gradient boosting.
- **Streamlit**: For building the web app interface.
- **Pandas**: For data manipulation.
- **Matplotlib**, **Seaborn**: For data visualization.
- **Dataset**: Clinical dataset containing features like age, cholesterol, and more.

## Dataset Information
The dataset contains key features that help in predicting heart disease. Some of the most important columns include:

- **Age**: The age of the patient.
- **Sex**: Gender of the patient.
- **Chest Pain Type**: The type of chest pain experienced (categorical).
- **Cholesterol**: Serum cholesterol in mg/dl.
- **Resting Blood Pressure**: Blood pressure at rest.
- **Max Heart Rate**: Maximum heart rate achieved during exercise.
- **Target**: Whether the patient has heart disease (binary: 0 or 1).

## Models
The following ensemble models were used for predicting heart disease:

- **Random Forest**: A bagging technique that builds multiple decision trees and averages their predictions.
- **Gradient Boosting**: A sequential boosting algorithm that focuses on correcting errors made by previous models.
- **XGBoost**: An optimized implementation of Gradient Boosting that improves both speed and performance.

### Model Evaluation Metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **ROC-AUC Score**


## How to Use the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SunnyBibyan/Heart_Disease_Prediction.git
   cd Heart_Disease_Prediction
   
2. **Install Dependencies**: Install all required libraries by running:
   ```bash
   pip install -r requirements.txt
5. **Run the Streamlit App**: Launch the app with the following command:
   ```bash
   streamlit run app.py

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect with Me
- **LinkedIn**: [Sunny Kumar](https://linkedin.com/sunny-bibyan)
- **Contact**: Email me at sunnykumar6121997@gmail.com


