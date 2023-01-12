a=int(input("total no of classes:"))
b=int(input("no of classes atended:"))
d=input("do yo have a medical issue?(Y/N):")
c=(b/a*100)
if(c>=75):
   print("you are eligible")
elif(c<=75 and d=='Y'):
   print("you are eligible")
elif(c<=75 and d=='N'):
   print("you are not eligible")
