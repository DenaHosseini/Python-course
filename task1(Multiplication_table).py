def multiplication_table():
    n = int(input("NUMBER OF ROWS :"))
    m = int(input("NUMBER OF COLUMNS :"))
    for i in range(1, n+2):
        for j in range(1, m+2):
            if i == 1 and j == 1:
                print('X', end='\t')
            elif i == 1:
                print(j-1, end='\t')
            elif j == 1:
                print(i-1, end='\t')
            else:
                print((i-1)*(j-1), end='\t')
        print()

print("WELCOME TO MULTIPLICATION TABLE MAKER!")
print("ENTER THE NUMBER OF ROWS AND COLUMNS OF THE MULTIPLICATION TABLE YOU WANT:)")
multiplication_table()
