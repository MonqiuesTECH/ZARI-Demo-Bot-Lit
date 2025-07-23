from flask import Flask, request
from zari_bot_voice import ask_zari

app = Flask(__name__)

@app.route('/')
def index():
    return "ZARI Lite is running."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return {"answer": ask_zari(question)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
