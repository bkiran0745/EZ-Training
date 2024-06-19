count = 0
num = int(input())
for i in range(1,int(num / 2)+1):
    if num % i == 0:
        count = 1
        break
if count == 1:
    print("Not Prime")
else:
    print("Prime")
