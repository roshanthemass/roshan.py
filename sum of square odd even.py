l=[]
n=int(input("no of list:"))
for i in range(n):
    b=int(input("enter the list:"))
    l.append(b)
def sumsq(l):
   odd=0
   even=0
   for i in l:
       if i%2==0:
           even = even + i**2
       else:
           odd = odd + i**2
   l=[odd,even]
   return(l)
print(sumsq(l))
