import json
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from utils.preprocess import clean_text, tokenize_and_lemmatize

class BotTrainer:
    def __init__(self, intent_path, model_output_path):
        self.intent_path = intent_path
        self.model_output_path = model_output_path

    def load_data(self):
        with open(self.intent_path, 'r') as file:
            intents = json.load(file)

        patterns = []
        labels = []

        for intent in intents['intents']:
            for pattern in intent['patterns']:
                patterns.append(clean_text(pattern))
                labels.append(intent['tag'])

        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(labels)
        return patterns, labels, label_encoder
    
    def train_model(self):
        
        patterns, labels, label_encoder = self.load_data()

        tokenizer = tf.keras.preprocessing.text.Tokenizer(num_word=1000)
        tokenizer.fit_on_texts(patterns)
        sequences = tokenizer.texts_to_sequences(patterns)
        data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=20)

        # Modelo
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(input_dim=1000, output_dim=64, input_length=20),
            tf.keras.layers.LSTM(64),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
        ])

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(data, labels, epochs=50, batch_size=8)

        # Guardar el modelo y el tokenizador
        model.save(self.model_output_path)
        print(f"Modelo guardado en {self.model_output_path}")
        return model