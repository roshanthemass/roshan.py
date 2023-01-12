a=int(input("How much years you worked here?:"))
b=int(input("enter your salary:"))
c=(b*5/100)
if(a>5):
   print("net bonus",c)
   print("net salary",b+c)
elif(a<5):
   print("net salary",b)
