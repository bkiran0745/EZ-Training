if int(input())%2 == 0:
    print("Even")
else:
    print("Odd")
for i in range(1,int(input())):
    if i%2 == 0:
        print(i," is even")
    else:
        print(i," is odd")
num = int(input())
num2 = int(num / 2)
for i in range(1,num2):
    if num % i == 0:
        count = 1
        break
if count == 1:
    print("Not Prime")
else:
    print("Prime")

a = int(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
count = 0
for a in range(1850 , 2025):
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        count += 1
print(count)