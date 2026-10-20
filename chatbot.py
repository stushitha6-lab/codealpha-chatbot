def chatbot():
    print("Chatbot: Hello! Welcome!")
    while True:
        user = input("You:").lower()
        if user == "hello":
            print("Chatbot:Hi!")
        elif user == "how are you":
            print("Chatbot:I'am fine,thanks!")
        elif user == "bye":
            print("Chatbot:Sorry, I don't understand.")

chatbot()
