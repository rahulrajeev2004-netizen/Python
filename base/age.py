age=int(input("Enter the age:"))
print("*"*(50))
if age >=1 and age <=12:
    print("You are child")
    print("*"*(50))
elif age >=13 and age <=19:
    print("You are teenager")
    print("*"*(50))
elif age >=20 and age <=40:
    print("You are adult")
    print("*"*(50))
elif age >=41 and age <=56:
    print("You are elder")
    print("*"*(50)) 
else:
    print("You are senior")
    print("*"*(50))            
    