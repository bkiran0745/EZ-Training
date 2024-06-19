# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
s = list(map(int,input().split()))
n1 = int(input())

lis = list()
for i in range(1,n1+1):
    lis2 = list(map(int,input().split()))
    lis.append(lis2)
sum = 0
coun = Counter(lis)
print(coun)