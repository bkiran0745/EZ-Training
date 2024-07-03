s = [1,4,4,5,3,2,1,3]
count = [0 for _ in range(6)]
print(count)
for i in s:
    count[i]+=1
print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
