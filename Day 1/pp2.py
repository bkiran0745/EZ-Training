#trio
def trio(l):
    l.sort()
    s = l[2]+l[1]
    return s
l = list(map(int,input().split()))
print(trio(l))