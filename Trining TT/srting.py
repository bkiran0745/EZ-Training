l=int(input())
s=input()
n=int(input())
if l==0 or s=="":
    print("NULL")
elif n==0:
    print(s)
else:
    res = ""
    #  n=n//1
    i = n
    while i<l:
        res += s[i]
        # print(res)
        i += 1
    i = 0
    while i<n:
        res += s[i]
        i += 1
    # res=s[n:]+s[:n]
    # print(s[:n])
    print(res)

