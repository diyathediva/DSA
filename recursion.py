n = int(input("What is n"))

sum = 0
for i in range(1,n+1):
    print(i)
    sum = sum + i
print(sum)

#recursion
def total(n):
    if n == 1:
        return 1
    else:
        return n+total(n-1)
 
print(total(n))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print("Series",fib(n))