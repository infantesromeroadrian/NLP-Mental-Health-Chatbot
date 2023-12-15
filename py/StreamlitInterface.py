import streamlit as st
from EmotionalChatBotModel import EmotionalChatbotModel

# Create an instance of the chatbot model
model_name = "Mohammed-Altaf/Medical-ChatBot"
chatbot_model = EmotionalChatbotModel(model_name)

st.title("Emotional Health Chatbot")

# Create a text box for user input
user_input = st.text_input("How can I help you today?")

if user_input:
    # Generate a response from the chatbot model
    response = chatbot_model.generate_response(user_input)

    # Display the chatbot response
    st.text_area("Chatbot says:", value=response, height=100, max_chars=None, key=None)
