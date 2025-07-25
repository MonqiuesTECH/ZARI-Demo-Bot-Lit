# app.py (final version with Flask + Gradio, clean routing)
from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr
from gradio.routes import mount_gradio_app
app = Flask(__name__)

# Gradio UI setup
def chat_with_zari(question):
    return ask_zari(question)

demo = gr.Interface(
    fn=chat_with_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)
# Mount Gradio at root
mount_gradio_app(app, demo, path="/")

# API endpoint for programmatic access
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})
# Entry point
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
