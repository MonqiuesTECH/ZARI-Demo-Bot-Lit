from flask import Flask, request, jsonify, render_template_string
from zari_bot_voice import ask_zari
import gradio as gr
import threading

app = Flask(__name__)

# Gradio Interface
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# Run Gradio in a separate thread
def run_gradio():
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False, inbrowser=False)

threading.Thread(target=run_gradio).start()

# Main homepage
@app.route("/")
def index():
    return render_template_string("<h1>ZARI is live.</h1><a href='http://localhost:7860' target='_blank'>Launch UI</a>")

# API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Entrypoint
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
