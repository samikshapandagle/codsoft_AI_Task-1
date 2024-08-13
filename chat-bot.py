import nltk
import nltk.downloader
import re
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

info = [
    [r"my name is (.*)", ["Hello %1, how can I assist you today?",]],
    [r"hi|hey|hello", ["Hello, how can I help you?", "Hey there! What can I do for you?", "Hi! How can I assist you today?"]],
    [r"what is your name?", ["I am a chatbot created to assist you. You can call me Anything.",]],
    [r"how are you?", ["I'm Good. How are you?",]],
    [r"fine| i'm good", ["that's nice to hear that", "glad you're doing well", "awesome"]],
    [r"can you help me with (.*)", ["Sure, I can help you with %1. Please provide more details.",]],
    [r"sorry (.*)", ["It's okay. How can I assist you?",]],
    [r"thank you|thanks", ["You're welcome!", "Happy to help!"]],
    [r"quit", ["Bye! Have a great day!","Goodbye!"]],
    [r"(.*)", ["I'm sorry, I don't understand that. Can you rephrase?", "Could you please elaborate on that?"]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)

chatbot = RuleBasedChatbot(info)
def chat_with_bot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

chat_with_bot()
responses = {
    'greet': 'Hello! How can I help you?',
    'timings': 'We are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.',
    'fallback': 'I dont quite understand. Could you repeat that?',
}
while True:
    user_input = input().lower()
    if user_input == 'quit':
        print("Thank you for visiting.")
        break
    matched_intent = None
    for intent, pattern in responses.items():
        if re.search(pattern, user_input):
            matched_intent = intent
    key = 'fallback'
    if matched_intent in responses:
        key = matched_intent    
    print(responses[key])