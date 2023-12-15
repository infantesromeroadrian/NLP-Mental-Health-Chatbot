import gradio as gr

class GradioChatbotInterface:
    def __init__(self, chatbot_model):
        self.chatbot_model = chatbot_model

    def chat(self, message):
        response = self.chatbot_model.generate_response(message)
        return response

    def launch(self):
        interface = gr.Interface(
            fn=self.chat,
            inputs=gr.Textbox(lines=2, placeholder="Type a message..."),
            outputs="text",
            title="Chatbot",
            description="This is a chatbot interface."
        )
        interface.launch(share=True)  # Set 'share' to True to make the interface public

# Rest of your code to initialize and launch the chatbot interface

