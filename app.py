import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar modelo entrenado
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Predicción de Gastos Médicos", page_icon="💊", layout="centered")

st.title("💊 Predicción de Gastos Médicos")
st.write("Completa la información del paciente para estimar los **gastos médicos anuales**.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Edad del paciente", 0, 100, 30)
    bmi = st.number_input("Índice de masa corporal (BMI)", min_value=10.0, max_value=60.0, value=25.0)
    children = st.number_input("Número de hijos", min_value=0, max_value=10, value=0)

with col2:
    sex = st.radio("Género", ["male", "female"], horizontal=True)
    smoker = st.radio("¿Fuma?", ["yes", "no"], horizontal=True)
    region = st.selectbox("Región", ["southwest", "southeast", "northwest", "northeast"])

input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region]
})

if st.button("🔮 Predecir gastos médicos"):
    prediction = model.predict(input_data)[0]

    st.success("Predicción completada")
    st.metric(label="💰 Gastos médicos estimados", value=f"{prediction:,.2f} USD")
