import cowsay

cowsay.cow("Hello! Moo! Moo!")

while True:
    input_text = input("Chat, or type 'quit': ")
    if input_text.lower() == "quit":
        cowsay.cow("Goodbye! Moo! Moo! Moo!")
        break

    cowsay.cow(input_text + " Moo!")