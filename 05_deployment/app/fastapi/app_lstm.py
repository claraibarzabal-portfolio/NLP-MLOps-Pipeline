from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import h5py

# Cargar el modelo LSTM
model = load_model('model_lstm.h5')

# Cargar el tokenizer del archivo H5
with h5py.File('model_lstm.h5', 'r') as f:
    tokenizer_data = f['tokenizer'][()]
    tokenizer = pickle.loads(tokenizer_data)

# Iniciar la aplicación FastAPI
app = FastAPI()

# Definir la estructura de los datos de entrada
class Review(BaseModel):
    text: str

# Función para realizar la predicción
def predict_sentiment(text):
    try:
        # Preprocesar el texto
        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=100)

        # Realizar la predicción
        prediction = model.predict(padded_sequence)
        prediction_class = np.argmax(prediction, axis=1)[0]

        # Clasificar la predicción
        sentiment = 'Positiva' if prediction_class == 1 else 'Negativa'
        return sentiment
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {e}")

# Definir el endpoint para la predicción
@app.post('/predict')
def predict(review: Review):
    sentiment = predict_sentiment(review.text)
    return {"sentiment": sentiment}
