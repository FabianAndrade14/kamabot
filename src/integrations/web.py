from flask import Flask, request, jsonify
from core.bot import ChatBot

app = Flask(__name__)
bot = ChatBot("models/trained_model.h5", "data/intents/telegram.json")

@app.route('/chat', method=['POST'])
def chat():
    user_input = request.json.get('message')
    response = bot.get_response(user_input)
    return jsonify({ 'response': response })

if __name__ == '__main__':
    app.run(debug=True)