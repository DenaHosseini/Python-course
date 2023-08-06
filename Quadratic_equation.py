import math
def  Quadratic_equation():
    print("Hello!hear you can solve the quadratic equation only by entering the values.")
    while True:
        user_input = input("ENTER '1' TO START AND '2' TO EXIT:")
        if user_input == "1":
            a = int(input("Enter a:"))
            b = int(input("Enter b:"))
            c = int(input("Enter c:"))
            delta = b**2 - 4*a*c

            if delta > 0 :
                x1 = (-b +math.sqrt(delta)) / (2*a)
                x2 = (-b -math.sqrt(delta)) / (2*a)
                print ("X1 =",x1,"  X2 =",x2)

            elif delta == 0 :
                x = -b / (2*a)
                print ("X =",x)
                    
            else :
                print("NO REAL ROOTS")

        elif user_input == "2":
            print("BYE BYE!")
            break

        else :
            print ("INVALID CHARACTER!")

Quadratic_equation()


        


    