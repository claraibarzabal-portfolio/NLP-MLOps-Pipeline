import tensorflow as tf
import numpy as np
import streamlit as st
import os
import gdown

# ML stuff
from transformers import BertTokenizer, TFBertForSequenceClassification
from tensorflow import keras

# preprocessing library
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, lower_text, remove_eol_characters, replace_currency_symbols, \
                                        remove_punct, remove_multiple_spaces_and_strip_text, filter_non_latin_characters

GOOGLE_DRIVE_FILE_ID = "YOUR_GOOGLE_DRIVE_FILE_ID_HERE"

# set maximum length and tokenizer
MAX_LEN = 50
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# stemmer
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword
stopword_factory = StopWordRemoverFactory()
stopword = stopword_factory.create_stop_word_remover()

# use nlpretext processor
preprocessor = Preprocessor()
preprocessor.pipe(lower_text)
preprocessor.pipe(remove_eol_characters)
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(remove_multiple_spaces_and_strip_text)
preprocessor.pipe(remove_punct)
preprocessor.pipe(replace_currency_symbols)
preprocessor.pipe(filter_non_latin_characters)

# load model on first launch
@st.cache(allow_output_mutation=True)
def load_model():
    filepath = "model/model.h5"

    # folder exists?
    if not os.path.exists('model'):
        # create folder
        os.mkdir('model')
    
    # file exists?
    if not os.path.exists(filepath):
        # download file
        url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
        gdown.download(url, filepath, quiet=False)
    
    # load model
    model = keras.models.load_model(filepath, custom_objects={"TFBertForSequenceClassification": TFBertForSequenceClassification})
    return model

def cleanText(sentence):
    # process with PySastrawi first
    stemmed = stemmer.stem(sentence)
    stopwordremoved = stopword.remove(stemmed)

    # then with nlpretext
    cleaned = preprocessor.run(stopwordremoved)

    # return
    return cleaned

def encodeText(sentence):
    sentence = cleanText(sentence)

    encoded_dict = tokenizer.encode_plus(
                    sentence,
                    add_special_tokens=True,
                    max_length=MAX_LEN,
                    truncation=True,
                    padding="max_length",
                    return_attention_mask=True,
                    return_token_type_ids=False
    )

    input_ids = [encoded_dict['input_ids']]
    attn_mask = [encoded_dict['attention_mask']]
      
    return input_ids, attn_mask

def predict(model, input):
    input_id, attn_mask = encodeText(input)
    input_id = np.array(input_id)
    attn_mask = np.array(attn_mask)

    # Make sure the input shapes are correct
    input_id = tf.convert_to_tensor(input_id)
    attn_mask = tf.convert_to_tensor(attn_mask)

    data = [input_id, attn_mask]

    prediction = model(data, training=False)
    prediction = tf.nn.softmax(prediction.logits, axis=-1)
    predicted_class = np.argmax(prediction, axis=1)[0]

    return predicted_class

# Streamlit UI
st.title("Clasificación de Reseñas con BERT")

# Campo de entrada de texto
user_input = st.text_area("Escribe una reseña")

# Botón para realizar la predicción
if st.button("Clasificar"):
    if user_input.strip() != "":
        model = load_model()
        prediction = predict(model, user_input)

        # Mostrar el resultado
        if prediction == 1:
            st.success("Esta reseña es positiva")
        elif prediction == 0:
            st.error("Esta reseña es negativa")
        else:
            st.warning("Esta reseña es neutral")
    else:
        st.warning("Por favor, ingresa una reseña para clasificar.")
