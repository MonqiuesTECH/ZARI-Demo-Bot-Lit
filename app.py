from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr
from gradio.routes import mount_gradio_app

app = Flask(__name__)

# Wrapper for Gradio logic
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

# API access
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Root HTML page
@app.route("/")
def index():
    return '''
    <html>
        <head><title>ZARI Lite</title></head>
        <body>
            <h2>ZARI is running</h2>
            <p><a href="/gradio">Click here to open the UI</a></p>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
