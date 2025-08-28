age=int(input("Enter the age:"))
print("*"*(50))
if age <= 17:
    print("You can't vote")
elif age == 18:
    print("You can vote but still you are in teenage")
elif age >=19:
    print("You are eligible for voting") 
else:
    pass   
print("*"*(50))       