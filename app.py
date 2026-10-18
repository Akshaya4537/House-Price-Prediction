import streamlit as st

st.title("🏠 House Price Prediction")

st.write("Enter the house details to estimate its price.")

area = st.number_input("House Area (sq ft)", min_value=100, value=1000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, value=1)

if st.button("Predict Price"):
    st.info("Next, we will connect your trained machine learning model here.")
