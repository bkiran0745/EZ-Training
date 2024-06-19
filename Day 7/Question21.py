#Count of Maximum vowels
from collections import Counter
def countOfOvels(str):
    lis = Counter(str)
    lis2 = list()
    for i,v in lis.items():
        if i in 'aeiou':
            lis2.append(v)
    return max(lis2)
srt = input()
print(countOfOvels(srt))
