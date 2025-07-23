from flask import Flask, request
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# Chat API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return {"answer": ask_zari(question)}

# Gradio UI
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

@app.route("/", methods=["GET"])
def gradio_ui():
    return demo.launch(share=False, inline=True, inbrowser=False, prevent_thread_lock=True, server_name="0.0.0.0", server_port=8000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
