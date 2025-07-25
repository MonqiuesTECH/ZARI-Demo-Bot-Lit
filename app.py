from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr
from gradio.routes import mount_gradio_app

app = Flask(__name__)

# Function that wraps the bot
def chat_with_zari(question):
    return ask_zari(question)

# Gradio UI
demo = gr.Interface(
    fn=chat_with_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# Mount Gradio at /gradio
mount_gradio_app(app, demo, path="/gradio")

# REST API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Root route
@app.route("/")
def index():
    return "<h2>ZARI is live. Visit the UI at <a href='/gradio'>/gradio</a></h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
