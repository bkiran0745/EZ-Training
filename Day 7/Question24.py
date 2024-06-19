a = int(input())
b = 1
lis = [1]
for i in range(2,a+1):
    b =b+i*2
    lis.append(b)
print(sum(lis))