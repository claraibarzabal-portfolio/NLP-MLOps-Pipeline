from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf
import numpy as np
import os
import gdown

# preprocessing library
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, lower_text, remove_eol_characters, replace_currency_symbols, \
                                        remove_punct, remove_multiple_spaces_and_strip_text, filter_non_latin_characters

# Initialize FastAPI
app = FastAPI()

# set maximum length 
MAX_LEN = 50
# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load model using caching
model = None

def load_model():
    global model
    filepath = "model/model.h5"

    if not os.path.exists('model'):
        os.mkdir('model')

    if not os.path.exists(filepath):
        url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
        gdown.download(url, filepath, quiet=False)

    model = tf.keras.models.load_model(filepath, custom_objects={"TFBertForSequenceClassification": TFBertForSequenceClassification})

# Stemmer and stopwords remover
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

stopword_factory = StopWordRemoverFactory()
stopword = stopword_factory.create_stop_word_remover()

# Text preprocessing using nlpretext
preprocessor = Preprocessor()
preprocessor.pipe(lower_text)
preprocessor.pipe(remove_eol_characters)
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(remove_multiple_spaces_and_strip_text)
preprocessor.pipe(remove_punct)
preprocessor.pipe(replace_currency_symbols)
preprocessor.pipe(filter_non_latin_characters)

def clean_text(sentence):
    stemmed = stemmer.stem(sentence)
    stopword_removed = stopword.remove(stemmed)
    cleaned = preprocessor.run(stopword_removed)
    return cleaned

def encode_text(sentence):
    sentence = clean_text(sentence)
    encoded_dict = tokenizer.encode_plus(
        sentence,
        add_special_tokens=True,
        max_length=MAX_LEN,
        truncation=True,
        padding="max_length",
        return_attention_mask=True,
        return_token_type_ids=False,
        return_tensors='tf'
    )
    input_ids = encoded_dict['input_ids']
    attn_mask = encoded_dict['attention_mask']
    return input_ids, attn_mask

def predict(input_text):
    if model is None:
        load_model()
    input_ids, attn_mask = encode_text(input_text)
    prediction = model([input_ids, attn_mask], training=False)
    prediction = tf.nn.softmax(prediction.logits, axis=-1)
    predicted_class = np.argmax(prediction, axis=1)[0]
    return predicted_class

# Endpoint for sentiment analysis
class SentimentRequest(BaseModel):
    text: str

@app.post("/predict/")
def analyze_sentiment(request: SentimentRequest):
    try:
        prediction = predict(request.text)
        return {"sentiment": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
