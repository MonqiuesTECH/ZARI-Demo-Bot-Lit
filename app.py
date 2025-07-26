from flask import Flask, request, jsonify, render_template_string
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# Gradio UI
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# Just link to the Gradio route
@app.route("/")
def index():
    return render_template_string("<h1>ZARI is live.</h1><a href='/gradio'>Launch UI</a>")

# Programmatic API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Run Gradio on /gradio
@app.route("/gradio")
def gradio_route():
    return demo.launch(
        share=False,
        inline=True,
        inbrowser=False,
        prevent_thread_lock=True,
        server_name="0.0.0.0",
        server_port=8000
    )

# Entrypoint
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
