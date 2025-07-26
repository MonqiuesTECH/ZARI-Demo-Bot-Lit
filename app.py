from flask import Flask, request, jsonify
from zari_bot_voice import ask_zari
import gradio as gr
import threading

app = Flask(__name__)

# Programmatic API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": ask_zari(question)})

# Gradio UI function
def launch_gradio():
    demo = gr.Interface(
        fn=ask_zari,
        inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
        outputs="text",
        title="ZARI Agent",
        description="Ask ZARI about your business, ops, or automation strategy."
    )
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,  # Use a different port to avoid Flask conflict
        share=False,
        inline=False
    )

@app.route("/")
def index():
    return 'ZARI is live.<br><a href="http://localhost:7860" target="_blank">Launch UI</a>'

# Start Flask + Gradio
if __name__ == "__main__":
    threading.Thread(target=launch_gradio).start()
    app.run(host="0.0.0.0", port=8000)
