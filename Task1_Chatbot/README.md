print("================================")
print("      THANMAI CHATBOT")
print("================================")

print("Chatbot is ready")
print("Type 'exit' to stop\n")

while True:

    text = input("You : ").lower()

    if text == "hi" or text == "hello":
        print("Bot : Hi")

    elif text == "how are you":
        print("Bot : I am fine. What about you")

    elif text == "what are you doing":
        print("Bot : Just talking with you")

    elif text == "had food":
        print("Bot : Not yet")

    elif text == "where are you":
        print("Bot : I am inside this program")

    elif text == "are you busy":
        print("Bot : No, I am free now")

    elif text == "do you like music":
        print("Bot : Yes, music feels relaxing")

    elif text == "what is your favorite color":
        print("Bot : I like black")

    elif text == "are you my friend":
        print("Bot : Yes, of course")

    elif text == "can we talk":
        print("Bot : Yes, we can talk")

    elif text == "good morning":
        print("Bot : Good Morning")

    elif text == "good night":
        print("Bot : Good Night")

    elif text == "thank you":
        print("Bot : Okay")

    elif text == "bye":
        print("Bot : Bye")

    elif text == "exit":
        print("Bot : Chat closed")
        break

    else:
        print("Bot : I did not understand")