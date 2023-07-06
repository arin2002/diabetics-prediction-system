import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Function to predict diabetes


def predict_diabetes(features):
    # Convert the features to a NumPy array and reshape it
    features = np.array(features).reshape(1, -1)
    # Make the prediction
    prediction = model.predict(features)
    # Return the prediction
    return prediction[0]

# Streamlit app


def main():
    # Set the title and description
    # st.title("Diabetes Prediction System")
    st.markdown(
        """
        <style>
        .title {
            font-family: 'Arial', sans-serif;
            color: #D42027;
            text-align: center;
            font-size: 36px;
            margin-bottom: 40px;
        }
        .description {
            font-family: 'Arial', sans-serif;
            color: #585858;
            text-align: center;
            font-size: 18px;
            margin-bottom: 40px;
        }
        .footer {
            font-family: 'Arial', sans-serif;
            color: #585858;
            text-align: center;
            font-size: 14px;
            margin-top: 40px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="title">Diabetes Prediction System</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="description">Enter the following information to predict the likelihood of diabetes.</div>', unsafe_allow_html=True)

    # Add some space and set the layout
    st.markdown("---")
    st.markdown(
        '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown(
        '<style>div.row-widget.stNumberInput > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # Create the input fields
    pregnancies = st.number_input(
        "Number of Pregnancies", min_value=0, max_value=20, value=0, step=1)
    glucose = st.number_input(
        "Glucose Level", min_value=0, max_value=200, value=100, step=1)
    blood_pressure = st.number_input(
        "Blood Pressure (mm Hg)", min_value=0, max_value=150, value=70, step=1)
    skin_thickness = st.number_input(
        "Skin Thickness (mm)", min_value=0, max_value=100, value=20, step=1)
    insulin = st.number_input(
        "Insulin Level (mu U/ml)", min_value=0, max_value=800, value=79, step=1)
    bmi = st.number_input("BMI", min_value=0.0,
                          max_value=60.0, value=25.0, step=0.1)
    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)

    # Create a feature array from the user input
    features = [pregnancies, glucose, blood_pressure,
                skin_thickness, insulin, bmi, diabetes_pedigree, age]

    # Create a button to predict diabetes
    if st.button("Predict"):
        # Call the predict_diabetes function with the user input features
        result = predict_diabetes(features)
        # Display the prediction
        if result == 0:
            st.markdown(
                '<p style="color:green; font-size:24px;">Good news! You are not likely to have diabetes.</p>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<p style="color:red; font-size:24px;">Warning! You are likely to have diabetes.</p>', unsafe_allow_html=True)

    # Add a footer
    st.markdown('<div class="footer">Made with ❤️ by Arin</div>',
                unsafe_allow_html=True)


# Run the app
if __name__ == '__main__':
    main()
