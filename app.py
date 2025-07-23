from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# API route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Gradio UI definition
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# Gradio UI route (mount it)
@app.route("/", methods=["GET"])
def index():
    return demo.launch(
        server_name=None,
        prevent_thread_lock=True,
        share=False,
        inline=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
