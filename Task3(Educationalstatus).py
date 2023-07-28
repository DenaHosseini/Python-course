print("How is your educational status? I will tell you!")
firstname = input("Enter your first name:")
lastname= input("Enter your last name:")
fullname = firstname +" "+ lastname + "!"
print("now please enter your grade of each course:")
C1= float(input("Course1: "))
while C1>20 or C1<0:
    C1=float(input("The range of grade can only be between 0-20!Enter again:"))
C2= float(input("Course2: "))
while C2>20 or C2<0:
     C2=float(input("The range of grade can only be between 0-20!Enter again:"))
C3= float(input("Course3: "))
while C3>20 or C3<0:
     C3=float(input("The range of grade can only be between 0-20!Enter again:"))
Avg = (C1+C2+C3)/3   
if Avg >= 17:
    print("Dear",fullname,"Congrats:)Your status is Great with",Avg,"Keep going!")
if Avg <17 and  Avg>=12:
    print("Dear", fullname,"Not bad;)Your status is normal with",Avg,"keep trying!")
if Avg < 12 :
        print("Dear",fullname,"unfortunately you Failed with",Avg,":( Try harder!")


