import streamlit as st
import joblib

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Function to predict diabetes
def predict_diabetes(features):
    # Reshape the features to match the model's expected input shape
    features = features.reshape(1, -1)
    # Make the prediction
    prediction = model.predict(features)
    # Return the prediction
    return prediction[0]

# Streamlit app
def main():
    # Set the title and description
    st.title("Diabetes Prediction System")
    st.write("Enter the following information to predict the likelihood of diabetes.")

    # Create input fields for user input
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=150, value=70)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=800, value=79)
    bmi = st.number_input("BMI", min_value=0, max_value=60, value=25)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)

    # Create a feature array from the user input
    features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age]

    # Create a button to predict diabetes
    if st.button("Predict"):
        # Call the predict_diabetes function with the user input features
        result = predict_diabetes(features)
        # Display the prediction
        if result == 0:
            st.write("Good news! You are not likely to have diabetes.")
        else:
            st.write("Warning! You are likely to have diabetes.")

# Run the app
if __name__ == '__main__':
    main()
