def word_counter():
    text = input("ENTER YOUR SENTENCE:")
    word_count = len(text.split(" "))
    print ("NUMBER OF WORDS:", word_count)

print("WELCOME! ENTER YOUR SENTENCE,I TELL YOU HOW MANY WORDS IT HAS.")
word_counter()