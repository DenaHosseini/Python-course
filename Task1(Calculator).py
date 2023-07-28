import math
print("Welcome to calculator program!")
print("choose one of the following operations:")
print("1.sin") 
print("2.cos")
print("3.tan")
print("4.cot")
print("5.factorial")
print("6.radical")
print("7.+")
print("8.-")
print("9.*")
print("10./")
OP= int(input("Enter the number of the OP you want to do:"))
if OP == 1 or OP == 2 or OP == 3 or OP == 4 or OP == 5 or OP == 6:
    num1 = int(input("Enter the number:"))
    if (OP == 1):
        print(math.sin("your answer is:",math.radians(num1)))
    elif (OP == 2):
         print(math.cos("your answer is:",math.radians(num1)))
    elif (OP == 3):
        print("your answer is:",math.tan(math.radians(num1)))
    elif (OP == 4):
        if math.tan(math.radians(num1))==0:
            print("undefined!") 
        else:
            print("your answer is:",1/math.tan(math.radians(num1)))
    elif (OP == 5):
            if (num1<0):
                print("it can't be negative!")
            else :
                print("your answer is:",math.factorial(num1))
    elif (OP == 6):
        if (num1<0):
            print("it can't be negative!")
        else:    
            print("your answer is:",math.sqrt(num1))
elif OP == 7 or OP == 8 or OP == 9 or OP == 10 :
    num2 = float(input("Enter first number: "))
    num3 = float(input("Enter second number: "))
    if OP == 7:
        print("your answer is:",num2 + num3)
    elif OP == 8:
        print("your answer is:", num2 - num3)
    elif OP == 9:
        print("your answer is:",num2 * num3)
    elif OP == 10:
        if num3 == 0:
            print("undefined!")
        else:
            print("your answer is:",num2 / num3)
else :
    print("invalid number intered!")






    
