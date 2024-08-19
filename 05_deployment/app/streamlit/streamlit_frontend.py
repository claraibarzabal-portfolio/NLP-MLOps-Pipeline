import streamlit as st
import requests

# Definir la URL del endpoint FastAPI
FASTAPI_URL = "http://localhost:8000/predict"

# Definir la interfaz de usuario de Streamlit
st.title("Clasificación de Reseñas con LSTM")

# Campo de entrada de texto
user_input = st.text_area("Escribe una reseña")

# Botón para realizar la predicción
if st.button("Clasificar"):
    # Verificar que el usuario haya ingresado un texto
    if user_input.strip() != "":
        try:
            # Enviar la solicitud POST a FastAPI
            response = requests.post(FASTAPI_URL, json={"text": user_input})
            response.raise_for_status()
            result = response.json()

            # Mostrar el resultado
            sentiment = result.get("sentiment")
            if sentiment == "Positiva":
                st.success("Esta reseña es positiva")
            elif sentiment == "Negativa":
                st.error("Esta reseña es negativa")
            else:
                st.warning("Resultado desconocido")
        except requests.exceptions.RequestException as e:
            st.error(f"Error al contactar al servicio: {e}")
    else:
        st.warning("Por favor, ingresa una reseña para clasificar.")
