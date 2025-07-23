from flask import Flask, request, Response
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

@app.route("/")
def index():
    return "ZARI Lite is running."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return {"answer": ask_zari(question)}

# Gradio UI (mounted manually, not launched as server)
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy.",
)

@app.route("/gradio")
def gradio_ui():
    return Response(demo.launch(
        server_name=None,
        prevent_thread_lock=True,
        inline=True,
        share=False,
        inbrowser=False
    ))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
