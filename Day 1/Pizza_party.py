def party(n,m):
    r = 999
    while r != 0:
        if n % m == 0:
            break
        m += 1
    return sum(map(int,str(m)))
n,m = map(int,input().split())
if n > m:
    print(party(n,m))