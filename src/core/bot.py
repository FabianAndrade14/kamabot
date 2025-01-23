import json
import random
import numpy as np
import tensorflow as tf
from utils.preprocess import clean_text, tokenize_and_lemmatize

class ChatBot:
    def __init__(self, model_path, intent_path):

        self.model = tf.keras.models.load_model(model_path)
        self.intents = self.load_intents(intent_path)
        self.tokenizer = self.load_tokenizer()

    def load_intents(self, intent_path):

        with open(intent_path, 'r') as file:
            return json.load(file)

    def load_tokenizer(self):

        words = []
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                words.extend(tokenize_and_lemmatize(pattern))
        tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=1000)
        tokenizer.fit_on_texts(words)
        return tokenizer

    def predict_intent(self, user_input):

        cleaned_input = clean_text(user_input)
        tokens = self.tokenizer.texts_to_sequences([cleaned_input])
        input_data = tf.keras.preprocessing.sequence.pad_sequences(tokens, maxlen=20)

        predictions = self.model.predict(input_data)
        intent_index = np.argmax(predictions)
        return self.intents['intents'][intent_index]['tag']

    def get_response(self, user_input):

        intent = self.predict_intent(user_input)
        for i in self.intents['intents']:
            if i['tag'] == intent:
                return random.choice(i['responses'])
        return "Lo siento, no entiendo esa pregunta."
