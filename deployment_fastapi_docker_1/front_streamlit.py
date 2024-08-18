import requests
import streamlit as st

# Definición de la URL de la API
API_URL = "http://localhost:8000/predict"

# Configuración de la página
st.title('Análisis de Sentimiento de Reviews')
st.markdown('Escribe una review y obtén una calificación de sentimiento:')

# Text Area para ingreso de usuario
review = st.text_area("Escribe tu review aquí:")

if st.button('Analizar review'):
    if review:
        # Preparar los datos para enviar a la API
        data = {"text": review}
        # Hacer la solicitud POST a la API
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            results = response.json()
            sentiment = results['sentiment']
            polarity = results['polarity']
            sentiment_polarity = results['sentiment_polarity']
            
            st.markdown("## Resultado del Análisis")
            st.markdown(f"**Sentimiento Predicho:** `{sentiment}`")
            st.markdown(f"**Polaridad:** `{polarity:.2f}`")
            st.markdown(f"**Clasificación del Sentimiento:** `{sentiment_polarity}`")

            if sentiment_polarity == 'Positivo':
                st.success("¡La review tiene un sentimiento positivo!")
            elif sentiment_polarity == 'Negativo':
                st.error("La review tiene un sentimiento negativo.")
            else:
                st.info("La review tiene un sentimiento neutral.")
            
        else:
            st.error("Error en la respuesta de la API")
    else:
        st.warning("Por favor, escribe una review para analizar.")

# Pie de página
# st.markdown("---")
# st.markdown("Desarrollado por el Grupo 1")



# import requests
# import streamlit as st

# # Definición de la URL de la API
# API_URL = "http://localhost:8000/predict"

# # Configuración de la página
# st.title('Análisis de sentimiento de reviews')
# st.markdown('Escribe una review y obtén una calificación de sentimiento: \n')
# review = st.text_area("Escribe tu review aquí:")  # Text Area para ingreso de usuario

# if st.button('Analizar review'):
#     if review:
#         # Preparar los datos para enviar a la API
#         data = {"text": review}
#         # Hacer la solicitud POST a la API
#         response = requests.post(API_URL, json=data)
#         if response.status_code == 200:
#             results = response.json()
#             sentiment = results['sentiment']
#             polarity = results['polarity']
#             sentiment_polarity = results['sentiment_polarity']
            
#             st.markdown(f"**Sentimiento:** {sentiment}")
#             st.markdown(f"**Polaridad:** {polarity:.2f}")
#             st.markdown(f"**Clasificación del Sentimiento:** {sentiment_polarity}")
#         else:
#             st.error("Error en la respuesta de la API")
#     else:
#         st.warning("Por favor, escribe una review para analizar.")

# Pie de página
# st.markdown("---")
# st.markdown("Desarrollado por [Tu Nombre](https://www.linkedin.com/in/tu-perfil)")
# st.markdown("Encuentra el código en [GitHub](https://github.com/tu-repo)")