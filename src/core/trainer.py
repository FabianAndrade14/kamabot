import json
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import numpy as np

class BotTrainer:
    def __init__(self, intent_path):
        self.intent_path = intent_path
    
    def train_model(self):
        with open(self.intent_path, 'r') as file:
            intents = json.load(file)
        
        patterns, labels = [], []
        for intent in intents['intents']:
            patterns.append(pattern)
            labels.appends(intent['tag'])

        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(labels)

        tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=1000)
        tokenizer.fit_on_texts(patterns)
        sequences = tokenizer.texts_to_sequences(patterns)
        data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=20)

        # Modelo
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(1000, 64, input_length=20),
            tf.keras.layers.LSTM(64),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(len(set(labels)), activation='softmax')
        ])

        model.compile(optimize='adam', loss='sparse_categorical_crossentropy', metric=['accuracy'])
        model.fit(data, np.array(labels), epochs=10)

        model.save("models/trained_model.h5")

        return model