year=int(input("Enter the year:"))
age=2025-year
print("*"*(50))   
if age < 18:
    print("You are teenager .You can't vote")
elif age ==18:
    print("Still your are teenager..but u can vote")
elif age >=19:
    print("You can vote")
print("*"*(50))            