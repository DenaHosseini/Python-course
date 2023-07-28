print("Welcome to triangle program!")
print("Instruction:enter 3 sides of your triangle then I will tell you whether it is possible to make it or not.")
side1=float(input("Enter the first side:"))
side2=float(input("Enter the second side:"))
side3=float(input("Enter the third side:"))
max=max(side1,side2,side3)
if max == side1:
    if side2 + side3> max:
        print("yes!")
    else:
        print("NO!")
if max == side2:
    if side1 + side3> max:
        print("yes!")
    else:
        print("NO!")
if max == side3:
    if side1 + side2> max:
        print("yes!")
    else:
        print("NO!")
        
