import math
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac
num = int(input())
print(math.factorial(num))
print(factorial(num))