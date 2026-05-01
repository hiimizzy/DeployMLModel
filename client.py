import streamlit as st
import requests

st.title("Iris Flower Prediction")

st.markdown(
    "Measurements of the iris flower (in cm):"
)

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1 )
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 6.9, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)   

if st.button("Predict"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Iris Class: {result['predicted_class']}")    
    else:
        st.error("Error in prediction. Please try again.")

# streamlit run client.py