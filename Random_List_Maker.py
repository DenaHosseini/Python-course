import random
print("WELCOME TO RANDOM LIST MAKER!")
n = int(input("How many numbers do you want your list have? "))
Unique_array = []
while len(Unique_array) < n:
    number = random.randint(1,n+10)
    if number not in Unique_array :
        Unique_array.append(number)
result = Unique_array
print("your list is ready:", result)
