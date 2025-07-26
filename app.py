from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr

app = Flask(__name__)

# Create Gradio interface
demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)
# Mount Gradio to a Flask route (works on single port!)
@app.route("/")
def index():
    return '''
        <h1>ZARI is live.</h1>
        <p><a href="/gradio">Launch UI</a></p>
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Run Flask app and mount Gradio app
if __name__ == "__main__":
    import gradio.routes
    from gradio.routes import mount_gradio_app

    app = mount_gradio_app(app, demo, path="/gradio")
    app.run(host="0.0.0.0", port=8000)
