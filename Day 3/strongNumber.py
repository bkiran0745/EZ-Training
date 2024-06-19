import math
def strongNumber(num):
    sumOfdigit = 0
    while num > 10:
        sumOfdigit += math.factorial(num%10)
        num //= 10
        if num < 10:
            sumOfdigit += num
    return sumOfdigit
num = int(input())
if num == strongNumber(num):
    print("it is Strong Number")
else:
    print("it is not Strong Number")