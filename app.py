from flask import Flask, request, jsonify, redirect
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# Gradio interface
def chat_with_zari(question):
    return ask_zari(question)

demo = gr.Interface(
    fn=chat_with_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# API route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# HTML landing page
@app.route("/")
def index():
    return """
    <html>
      <head><title>ZARI Agent</title></head>
      <body>
        <h1>ZARI Lite is running.</h1>
        <p>Click to launch: <a href='/gradio'>Open ZARI UI</a></p>
      </body>
    </html>
    """

# Gradio route
@app.route("/gradio")
def gradio():
    return demo.launch(share=False, inline=True, inbrowser=False, prevent_thread_lock=True)

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
