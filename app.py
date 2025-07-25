from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# Gradio UI function
def chat_with_zari(question):
    return ask_zari(question)

demo = gr.Interface(
    fn=chat_with_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

@app.route("/")
def index():
    return demo.launch(share=False, inline=True, inbrowser=False, prevent_thread_lock=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
