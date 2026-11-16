import re
import random

RULES = [
    (r"\b(hello|hi|hey)\b", ["Hello! How can I help you?", "Hi! Nice to meet you."]),
    (r"\bhow are you\b", ["I am fine. Thank you!", "I am doing great."]),
    (r"\bmy name is (.*)", ["Nice to meet you, {}!"]),
    (r"\bi am (.*)", ["Why do you say you are {}?"]),
    (r"\bwhat is your name\b", ["I am a simple Python chatbot."]),
    (r"\b(thank you|thanks)\b", ["You are welcome!"]),
    (r".*\?", ["That is an interesting question."])
]

DEFAULT_RESPONSES = [
    "Sorry, I did not understand.",
    "Please tell me more."
]

print("Chatbot: Hello! Welcome to the chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()
    if user_input in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye! Have a nice day.")
        break
        
    user_input = re.sub(r'[^\w\s?]', '', user_input)
    matched = False
    
    for pattern, responses in RULES:
        match = re.search(pattern, user_input)
        if match:
            response = random.choice(responses)
            if "{}" in response:
                response = response.format(match.group(1).strip())
            print("Chatbot:", response)
            matched = True
            break
            
    if not matched:
        print("Chatbot:", random.choice(DEFAULT_RESPONSES))