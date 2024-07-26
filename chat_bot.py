import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program :)"]
    ],
    [
        r"(.*) (location|city) ?",
        ["Tokyo, Japan"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I don't have health. But thanks for asking!"]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. Goodbye!"]
    ],
    # New pairs you requested:
    [
        r"what's the weather like today",
        ["I'm sorry, I don't have real-time weather information."]
    ],
    [
        r"good morning",
        ["Good morning! How can I assist you today?"]
    ],
    [
        r"tell me a joke",
        ["Sure! Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"goodbye",
        ["Goodbye! Have a great day!", "Take care! See you next time!"]
    ],
]

def chatbot():
    print("Hi, I'm Chatbot! How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')  # Ensure tokenizer is available
    chatbot()
