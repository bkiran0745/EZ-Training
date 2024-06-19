def reverse(n):
    rev = 0
    while n > 10:
        rev = rev+n%10
        rev *= 10
        n = n//10
        if n < 10:
            rev = rev + n
    return rev
num = int(input())
print(reverse(num))