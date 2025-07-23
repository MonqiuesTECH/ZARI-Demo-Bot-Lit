import gradio as gr
from zari_bot_voice import ask_zari

demo = gr.Interface(
    fn=ask_zari,
    inputs=gr.Textbox(lines=2, placeholder="Ask ZARI anything..."),
    outputs="text",
    title="ZARI Agent",
    description="Ask ZARI about your business, ops, or automation strategy."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)
