p = int(input("Enter the amount: "))
t = float(input("Enter the number of years: "))
s = input("is coustomer senior citizen: ")
r=0
if(s=="yes"):
    r+=12
else:
    r+=10
SimpleInterset = (p*t*r)/100
print("The simple interset is:", SimpleInterset)
