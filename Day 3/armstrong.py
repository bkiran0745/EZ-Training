def Armstrong(n):
    sum = 0
    tem = n
    c = 0
    count = []
    while n > 10:
        sum +=n%10
        c += 1
        count.append(n%10)
        n //= 10
        if n<10:
            sum +=n
            c +=1
            count.append(n%10)
    sum = 0
    for i in count:
        sum +=i**c
    if tem == sum:
        return True
num = int(input())
if Armstrong(num):
    print("It is armstrong")
else:
    print("It is not armsstrong")    