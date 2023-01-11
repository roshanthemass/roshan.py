n = int(input("Enter the number:"))
a = n
b = 0
while(n>0):
    c = n % 10
    b = b*10 + c
    n = n // 10
if(a == b):
    print("Palindrome")
else:
    print("Not a Palindrome")
