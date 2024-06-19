'''You are given a string containing words separated by spaces. Your 
task is to write a
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello'''
s = input()
def revers(s):
    words = s.split()
    words.reverse()
    return words
print(*revers(s))
#or
print(' '.join(s.split()[::-1])) #using slicing