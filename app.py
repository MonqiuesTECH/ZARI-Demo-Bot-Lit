from flask import Flask, request
import gradio as gr
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

demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI Agent anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI Agent about your business, ops, or automation strategy."
)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
