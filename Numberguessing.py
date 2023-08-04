import random
print("WELCOME TO NUMBER GUESSING GAME!you have 10 chances to reach the secret number.")
PC_number = random.randint(0, 20)
count = 0
for i in range(10):
    user_number = int(input("Enter your guess number:"))
    count+=1
    if user_number == PC_number :
        print("YOU WON!you had", count , "guess(es).")
        if count == 1:
            print("YOU ARE NOSTRADAMUS!")
        break
    if user_number < PC_number :
        if count == 10:        
            print("YOU LOSE!")
        else:
            print("go higher!")
    if user_number > PC_number :
        if count == 10:        
            print("YOU LOSE!")
        else:
            print("go lower!")
