def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
def c(s):
    return fib(s + 1)
s=int(input("value of n"))
print ("Number of ways = ",c(s))

