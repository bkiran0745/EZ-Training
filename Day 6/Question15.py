#Prime number using squrt method
import math
num = int(input())
snum = math.sqrt(num)
count = 1
for i in range(2,int(snum)+1):
    if num%i == 0:
        count = 0
if count == 0:
    print('not prime')
else:
    print('prime')