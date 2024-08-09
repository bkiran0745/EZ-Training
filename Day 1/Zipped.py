# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
l = list()
for i in range(m):
    s = list(map(float, input().split()))
    l.append(s)
res = []
k = 0
j = 0
su = 0
while k != n:
    su += l[j][k]
    j += 1
    if j == m:
        j = 0
        k += 1
        res.append(su / m)
        su = 0
for i in res:
    print(i)