def even(n):
    if n%2==0:
        return True
    else:
        return False
num = int(input())
if even(num):
    print("This is even")
else:
    print("not")