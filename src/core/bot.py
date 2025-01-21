import json
import random

class ChatBot:
    def __init__(self, model_path, intent_path):
        self.model_path = model_path
        self.intent_path = intent_path
        self.intents = self.load_intents()

    def load_intents(self):
        with open(self.intent_path, 'r') as file:
            return json.load(file)
    
    def get_response(self, user_input):
        for intent in self.intents['intents']:
            if user_input.lower() in intent['patterns']:
                return random.choice(intent['responses'])
        return "Lo siento, no entiendo la pregunta."
        