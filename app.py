import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("car_price_model.pkl")
columns = joblib.load("columns.pkl")

# Page config
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")

# Custom UI
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #7f8c8d;
}
.stButton>button {
    background-color: #3498db;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🚗 Car Price Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict used car price using Machine Learning</p>', unsafe_allow_html=True)

st.write("")

# Layout
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=1995, max_value=2025, value=2015)
    km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7])
    mileage = st.number_input("Mileage (km/l)", value=20.0)

with col2:
    engine = st.number_input("Engine (CC)", value=1200)
    power = st.number_input("Max Power (bhp)", value=80.0)
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Feature engineering
car_age = 2025 - year

# Prepare input dictionary
input_dict = {
    'year': year,
    'km_driven': km_driven,
    'seats': seats,
    'Mileage': mileage,
    'Engine (CC)': engine,
    'max_power (in bhp)': power,
    'car_age': car_age
}

# Initialize all columns with 0
for col in columns:
    if col not in input_dict:
        input_dict[col] = 0

# Handle fuel encoding
if 'fuel_Diesel' in columns and fuel == "Diesel":
    input_dict['fuel_Diesel'] = 1
if 'fuel_Petrol' in columns and fuel == "Petrol":
    input_dict['fuel_Petrol'] = 1
if 'fuel_LPG' in columns and fuel == "LPG":
    input_dict['fuel_LPG'] = 1

# Handle transmission encoding
if 'transmission_Manual' in columns and transmission == "Manual":
    input_dict['transmission_Manual'] = 1
if 'transmission_Automatic' in columns and transmission == "Automatic":
    input_dict['transmission_Automatic'] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Ensure column order matches training
input_df = input_df[columns]

# Prediction
if st.button("🚀 Predict Price"):
    prediction = model.predict(input_df)[0]
    prediction = max(prediction, 0)  # avoid negative price

    st.success(f"💰 Estimated Car Price: ₹ {int(prediction):,}")

st.markdown("""
---
<div style='text-align: center; padding: 15px;'>

<p style='font-size:18px; color:#2c3e50;'>
    🚀 Created by <b style='color:#16a085;'>Moh Azeem</b>
</p>

<a href="https://github.com/MohAzeem1" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30"/>
</a>

</div>
""", unsafe_allow_html=True)