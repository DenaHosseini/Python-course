import random
print("WELCOME TO DICE GAME")
print("if you got 6, you can roll twice, otherwise you only can role once.")
user_input =input("Enter '1' To start or '2' to exit:") 
roll = random.randint(1,6)
chances = 1
if user_input=="1" :
    while chances!=0:
        roll = random.randint(1,6)
        if roll == 6:
            chances = 1
            input2 = input("How lucky! you got 6! you can roll one more time;)Enter '1':")
            if input2 == "1":
                 roll
            else :
                 print("Invalid charecter!")
        else :  
            roll
            print("you rolled " , roll)
            chances = 0
elif user_input=="2" :
    print("Okay , have a good day!")
else :
        print("Invalid charecter!")


