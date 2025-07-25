from flask import Flask, request, jsonify
import threading
import gradio as gr
from zari_bot_voice import ask_zari

app = Flask(__name__)

# Gradio setup
def chat_with_zari(question):
    return ask_zari(question)

demo = gr.Interface(
    fn=chat_with_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

# Flask API route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Optional HTML landing page
@app.route("/")
def index():
    return """
    <html>
      <head><title>ZARI Lite</title></head>
      <body>
        <h1>ZARI is live.</h1>
        <p><a href="http://localhost:8000">Launch UI</a></p>
      </body>
    </html>
    """

# Run Gradio in a thread
def run_gradio():
    demo.launch(server_name="0.0.0.0", server_port=8000, share=False, prevent_thread_lock=True)

if __name__ == "__main__":
    threading.Thread(target=run_gradio).start()
    app.run(host="0.0.0.0", port=5000)
