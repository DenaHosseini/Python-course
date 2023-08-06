print("WELCOME TO CHESSBOARD GENERATOR!")
while True : 
    user_input =input("Enter '1' to start or '2' to exit:")
    if user_input == "1" :

        m = int(input("Enter the number of 'rows' you want:"))
        n = int(input("Enter the number of 'columns' you want:"))

        for i in range(m) :
            for i in range(n):
                print("#", end=" ")
            print()

    elif user_input == "2" :
        print("BYE BYE!")
        break

    else :
       print ("Invalid character!")  






