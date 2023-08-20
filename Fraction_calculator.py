print("Welcome to the fraction calculator!")

def create_fraction(fraction_num):
    s, m = 0, 0
    while m == 0:
        s = int(input(f"Enter the numerator of fraction {fraction_num}: "))
        m = int(input(f"Enter the denominator of fraction {fraction_num}: "))
        if m == 0:
            print("Denominator cannot be zero!")
    return {"s": s, "m": m}

def add(f1, f2) :
    result = {}
    result["s"] = (f1["s"] * f2["m"]) + (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result

def multiply(f1,f2):
    result = {}
    result["s"] = f1["s"] * f2["s"]
    result["m"] = f1["m"] * f2["m"]
    return result

def subtract(f1,f2):
    result = {}
    result["s"] = (f1["s"] * f2["m"]) - (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result

def divide(f1, f2) :
    result = {}
    result["s"] = f1["s"] * f2["m"]
    result["m"] = f1["m"] * f2["s"]
    return result

def show_menu():
    while True:
        print("The following operations are available:")
        print("_________________")
        print("----Main Menu----")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("_________________")
        user_choice = int(input("Enter option number: "))
        if user_choice not in range(1,6) :
            print("Please enter a valid option number (1-5)!")
            continue
        elif user_choice == 5:
            print("Bye!Have a good day.")
            break

        f1 = create_fraction(1)
        f2 = create_fraction(2)

        if user_choice == 1:
            result = add(f1,f2)
        elif user_choice == 2:
            result = subtract(f1,f2)
        elif user_choice == 3:
            result = multiply(f1,f2)
        elif user_choice == 4:
            result = divide(f1,f2)

        print("The result is:")
        show(result)

def show(fraction):
    decimal = fraction['s'] / fraction['m']
    print(f"{fraction['s']}/{fraction['m']} = {decimal:.2f}")

show_menu()

