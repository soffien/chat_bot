from flask import Blueprint, render_template, request, jsonify
from .model import SimpleChatbotModel

chatbot_model = SimpleChatbotModel()

app = Blueprint('app', __name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    if msg:
        response_message = get_Chat_response(msg)
        return jsonify({"response": response_message})
    return jsonify({"error": "No message received"}), 400

def get_Chat_response(text):
    response = chatbot_model.predict(text)
    return response

