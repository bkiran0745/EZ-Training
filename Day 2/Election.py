from collections import Counter
numberOfVotes = int(input())
countOfVotes = list(map(int,input().split()))
count =Counter(countOfVotes)

def counterForElection(count):
    storMaxCount = 0
    storMaxcountName = 0
    for i,val in count.items():
        if val == storMaxCount:
            return True
        if val > storMaxCount:
            storMaxCount = val
            storMaxcountName = i
    return storMaxcountName
n = counterForElection(count)
if n:
    print("not possible")
else:
    print(n)

# numberOfVotes = input()
# n = max()