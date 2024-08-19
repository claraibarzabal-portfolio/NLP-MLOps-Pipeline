import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import h5py
import pickle

# Cargar el modelo
model = load_model('model_lstm.h5')

# Cargar el tokenizer del archivo H5
with h5py.File('model_lstm.h5', 'r') as f:
    tokenizer_data = f['tokenizer'][()]
    tokenizer = pickle.loads(tokenizer_data)

# Definir la interfaz de usuario de Streamlit
st.title("Clasificación de Reseñas con LSTM")

# Campo de entrada de texto
user_input = st.text_area("Escribe una reseña")

# Botón para realizar la predicción
if st.button("Clasificar"):
    # Verificar que el usuario haya ingresado un texto
    if user_input.strip() != "":
        # Preprocesar la entrada del usuario
        sequence = tokenizer.texts_to_sequences([user_input])
        padded_sequence = pad_sequences(sequence, maxlen=100)

        # Realizar la predicción
        prediction = model.predict(padded_sequence)
        prediction_class = np.argmax(prediction, axis=1)[0]

        # Mostrar el resultado
        if prediction_class == 1:
            st.success("Esta reseña es positiva")
        else:
            st.error("Esta reseña es negativa")
    else:
        st.warning("Por favor, ingresa una reseña para clasificar.")

