from rapidfuzz import fuzz as fz
from rapidfuzz import process as fzpr

a = 0

while a==0:
    user_input = input("Send a message: ")  
    user_input = user_input.lower()

    intents = {"greeting":["hello", "hi", "good morning", "how are you", "hey"],
            "goodbye":["bye", "bbye", "see you", "see you later", "see you soon"],
            "ask_name":["what is your name", "whats your name"],
            "help":["help", "please help", "do this for me"],
            "time_request":["what is the time"],
            "unknown":[]
            }

    responses = {
        "greeting": "Hey! How can I help you?",
        "goodbye": "Goodbye! Have a great day!",
        "ask_name": "I'm a chatbot created by you!",
        "help": "Sure, what do you need help with?",
        "time_request": "I can't tell time yet, but you can check your clock!",
        "unknown": "Sorry, I didn't understand that."
    }


    def checkIntent(user_input):
        
        best_score = 0
        best_intent = None
        threshold = 80
        best_match = None
    
        for intent, phrases in intents.items():
            result = fzpr.extractOne(user_input, phrases)
            
            if result is not None:
                match, score, idx = result
            
            if score > best_score:
                best_intent = intent
                best_score = score
                best_match = match 

        if score >= threshold:
            return intent
        else:
            intent = "unknown"
            return intent



    out = checkIntent(user_input)

    if out == "greeting":
        print(responses["greeting"])
    elif out == "goodbye":
        print(responses["goodbye"])
    elif out == "ask_name":
        print(responses["ask_name"])
    elif out == "help":
        print(responses["help"])
    elif out == "time_request":
        print(responses["time_request"])
    else:
        print(responses["unknown"])
    
    if user_input in intents["goodbye"]:
        a = 1