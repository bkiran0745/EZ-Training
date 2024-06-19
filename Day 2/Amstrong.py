def Amstrong(n):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False
n = int(input())
if Amstrong(n):
    print("Amstrong Number")
else:
    print("Not Amstrong Number")