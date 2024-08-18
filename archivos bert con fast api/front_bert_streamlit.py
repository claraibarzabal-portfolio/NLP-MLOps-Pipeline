import streamlit as st
import requests

# Streamlit UI
st.title("Clasificación de Reseñas con BERT y TensorFlow")

# Campo de entrada de texto
user_input = st.text_area("Escribe una reseña")

# Botón para realizar la predicción
if st.button("Clasificar"):
    if user_input.strip() != "":
        try:
            # Hacer la solicitud POST al servidor FastAPI
            response = requests.post("http://localhost:8000/predict/", json={"text": user_input})
            
            if response.status_code == 200:
                result = response.json()
                sentiment = result["sentiment"]

                # Mostrar el resultado de la predicción
                if sentiment == 1:
                    st.success("Esta reseña es positiva")
                elif sentiment == 0:
                    st.error("Esta reseña es negativa")
                else:
                    st.warning("Esta reseña es neutral")
            else:
                st.error("Error al procesar la solicitud.")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error de conexión: {e}")
    else:
        st.warning("Por favor, ingresa una reseña para clasificar.")
