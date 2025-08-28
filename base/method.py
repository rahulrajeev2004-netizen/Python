fnumber=input("Enter the first number:")
lnumber=input("Enter the second number:")
method=input("Enter the method (+,-,*,/,%):")
x=int(fnumber)
y=int(lnumber)
print("*"*(50))
if method== "+":
 print("The result is:"+str(x+y))
elif method== "-":
  print("The result is:"+str(x-y))
elif method== "*":
   print("The result is:"+str(x*y))  
elif method== "/":
   print("The result is:"+str(x/y)) 
print("*"*(50))  
