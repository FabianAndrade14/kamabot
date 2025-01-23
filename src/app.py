import json
from core.bot import ChatBot
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargamos las configuraciones
with open("models/config.json", "r") as config_file:
    config = json.load(config_file)

@app.route('/chat/kamabot', methods=['POST'])
def chat(app_name):
    if app_name not in config["apps"]:
        return jsonify({"error": "App no configurada"}), 400
    
    app_config = config["apps"][app_name]
    bot = ChatBot(app_config["model_path"], app_config["intents_file"])

    user_input = request.json.get("message")
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)