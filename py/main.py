from EmotionalChatBotModel import EmotionalChatbotModel
from GradioInterface import GradioChatbotInterface

if __name__ == "__main__":
    model_name = "Mohammed-Altaf/Medical-ChatBot"
    chatbot_model = EmotionalChatbotModel(model_name)
    chatbot_interface = GradioChatbotInterface(chatbot_model)
    chatbot_interface.launch()