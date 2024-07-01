rote = [[1,2,2,3],
        [3,1,4,2],
        [1,5,3,3],
        [1,2,1,1]]
minsum = rote[0][0]
root = [[0,0]]
i = 0
j = 0
n = len(rote)-1
m = len(rote[0])-1
while(i<n or j<m):
    if i == n:
        j += 1
    elif j == m:
        i +=1
    elif rote[i][j+1] < rote[i+1][j]:
        j = j+1
    else:
        i = i+1
    minsum += rote[i][j]
    root.append([i,j])
print(minsum)
print(root)
   