print("     WELCOME TO DECODELABS AI ASSISTANT   ")
print("==========================================")
print("Type 'exit' at any time to end the chat.\n")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break
        
    elif user_input == "hello" or user_input == "hi":
        print("Bot: Hi there! How can I help you today?")
        
    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")
        
    elif user_input == "what is your name":
        print("Bot: I am a simple rule-based AI chatbot.")
        
    elif user_input == "who made you":
        print("Bot: I was developed by the AI engineering team at DecodeLabs!")
        
    elif user_input == "what can you do":
        print("Bot: I can answer basic questions using simple logic rules.")
        
    elif user_input == "help":
        print("Bot: You can ask my name, who made me, what AI is, or type 'exit'.")
        
    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence—machines trained to perform smart tasks!")
        
    elif user_input == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")
        
    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome! Glad I could help.")
        
    else:
        print("Bot: I don't understand that yet. Try typing 'help'.")