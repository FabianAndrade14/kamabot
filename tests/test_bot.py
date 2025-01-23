import unittest
from core.bot import ChatBot

class TestChat(unittest.TestCase):
    def test_response(self):
        bot = ChatBot("models/trained_model.h5", "data/intents/telegram.json")
        response = bot.get_response("Hola")
        self.assertIn(response, ["¡Hola!", "¿Cómo puedo ayudarte"])

if __name__ == '__main__':
    unittest.main()