from transformers import pipeline

class EmotionalChatbotModel:
    def __init__(self, model_name):
        self.model = pipeline("text-generation", model=model_name)

    def generate_response(self, input_text):
        response = self.model(input_text)[0]['generated_text']
        return response
