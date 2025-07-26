from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr
from gradio.routes import mount_gradio_app

app = Flask(__name__)

demo = gr.Interface(
    fn=ask_zari,
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
    return '''
        <h1>ZARI is live.</h1>
        <p><a href="/gradio">Launch UI</a></p>
    '''

if __name__ == "__main__":
    app = mount_gradio_app(app, demo, path="/gradio")
    app.run(host="0.0.0.0", port=8000)
