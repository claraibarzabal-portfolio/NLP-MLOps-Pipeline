import streamlit as st
import joblib

# Cargar el vectorizador y el modelo
vectorizer = joblib.load('tfidf_vectorizer.joblib')
model = joblib.load('naive_model.joblib')

st.title("Análisis de Sentimientos de Reviews de Aerolíneas")

# Entrada de usuario
user_input = st.text_area("Introduce la reseña de la aerolínea:")

if st.button("Predecir"):
    if user_input:
        # Preprocesar la entrada del usuario y hacer la predicción
        user_input_transformed = vectorizer.transform([user_input])
        prediction = model.predict(user_input_transformed)
        
        # Mapear la predicción a una etiqueta de sentimiento
        sentiment = "Negativo" if prediction[0] == 0 else "Positivo"
        
        st.write(f"Predicción: {sentiment}")
    else:
        st.write("Por favor, introduce una reseña.")

