rote = [[1,2,2,3],[3,1,4,2],[1,5,3,3],[1,2,1,1]]
s = [0 for _ in range(len(rote[1]))]
s[0] = rote[0][0]
dp = []
dp.append(s)
for i in range(1,len(rote)):  
    s = [0 for _ in range(len(rote[i]))]
    s[0] = dp[i-1][0]+rote[i][0]
    dp.append(s)
s = rote[0]
for i in range(1,len(rote[0])):
    s[i] = s[i-1]+rote[0][i]
dp.insert(0,s)
i,j = 1,1
dp.pop(1)
while i<len(rote):
    if dp[i][j] == 0:
        if dp[i-1][j] < dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + rote[i][j]
            j += 1
        else:
            dp[i][j] = dp[i][j-1] + rote[i][j]
            j += 1
    if j>len(rote[i])-1:
        j = 1
        i+=1
# print(*dp)
print(dp[-1][-1])