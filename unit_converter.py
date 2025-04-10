import streamlit as st

st.set_page_config(page_title="Daily Unit Converter", page_icon="🧮")
st.title("🧮 Simple Daily Unit Converter")

conversion = st.selectbox("Choose Conversion Type:", [
    "Meters to Kilometers",
    "Kilometers to Meters",
    "Grams to Kilograms",
    "Kilograms to Grams",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Minutes to Hours",
    "Hours to Minutes",
    "Kilometers/hour to Meters/second",
    "Meters/second to Kilometers/hour"
])

value = st.number_input("Enter the value:", step=0.1)

if st.button("Convert"):
    if conversion == "Meters to Kilometers":
        result = value / 1000
        st.success(f"{value} meters = {result} kilometers")
    elif conversion == "Kilometers to Meters":
        result = value * 1000
        st.success(f"{value} kilometers = {result} meters")
    elif conversion == "Grams to Kilograms":
        result = value / 1000
        st.success(f"{value} grams = {result} kilograms")
    elif conversion == "Kilograms to Grams":
        result = value * 1000
        st.success(f"{value} kilograms = {result} grams")
    elif conversion == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result}°F")
    elif conversion == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result:.2f}°C")
    elif conversion == "Minutes to Hours":
        result = value / 60
        st.success(f"{value} minutes = {result} hours")
    elif conversion == "Hours to Minutes":
        result = value * 60
        st.success(f"{value} hours = {result} minutes")
    elif conversion == "Kilometers/hour to Meters/second":
        result = value / 3.6
        st.success(f"{value} km/h = {result:.2f} m/s")
    elif conversion == "Meters/second to Kilometers/hour":
        result = value * 3.6
        st.success(f"{value} m/s = {result:.2f} km/h")