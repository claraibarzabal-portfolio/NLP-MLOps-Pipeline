from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import altair as alt

# Descargar las stopwords si aún no están descargadas
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Definir el path del modelo
model_path = 'logistic_regression_model.pkl'

# Función para limpiar el texto de las reseñas
def review_cleaning(text):
    '''Make text lowercase, remove text in square brackets, remove links, remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()  # Convertir el texto a minúsculas
    text = re.sub('\[.*?\]', '', text)  # Eliminar texto dentro de corchetes
    text = re.sub('https?://\S+|www\.\S+', '', text)  # Eliminar enlaces
    text = re.sub('<.*?>+', '', text)  # Eliminar etiquetas HTML
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Eliminar puntuación
    text = re.sub('\n', '', text)  # Eliminar saltos de línea
    text = re.sub('\w*\d\w*', '', text)  # Eliminar palabras que contienen números
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Eliminar stopwords
    return text

# Función para cargar el modelo
def load_model(model_path):
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"No se pudo cargar el modelo: {e}")

# Cargar el modelo 
model = load_model(model_path)

# Iniciar la aplicación FastAPI
app = FastAPI()

# Definir la estructura de los datos de entrada
class Review(BaseModel):
    text: str

# Función para realizar la predicción
def predict_sentiment(model, cleaned_text):
    try:
        prediction = model.predict([cleaned_text])[0]
        polarity = TextBlob(cleaned_text).sentiment.polarity
        sentiment_polarity = classify_sentiment(polarity)
        return {
            'sentiment': prediction,
            'polarity': polarity,
            'sentiment_polarity': sentiment_polarity
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {e}")

# Función para clasificar el sentimiento basado en la polaridad
def classify_sentiment(polarity):
    if polarity < 0:
        return 'Negativo'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Positivo'

# Definir el endpoint para la predicción
@app.post('/predict')
def predict(review: Review):
    # Preprocesar el texto de la reseña
    cleaned_text = review_cleaning(review.text)
    
    # Realizar la predicción y retornar el resultado
    return predict_sentiment(model, cleaned_text)