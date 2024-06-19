'''8) Smallest Number
Prince participated in three Olympiads at school and received marks 
for all of them. 
He is interested in finding out the lowest mark he obtained among 
the three Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''
lis = list(map(int,input().split()))
def findingMin(lis):
    min1 = lis[0]
    for i in lis:
        if min1 > i:
            min1 = i
    return min1
print(findingMin(lis))