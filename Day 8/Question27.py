'''Pangram is a sentence containing every letter in the English alphabet. 
Given a string, 
find all characters that are missing from the string, Le., the characters 
that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz'''
a = 'abcdefghijklmnopqrstuvwxyz'
char = []
for ascii_value in range(97, 123):  # ASCII values for lowercase letters
    char.append(chr(ascii_value))
def find(str1):
    s = ''
    for i in char:
        if i not in str1:
            s+=i
    return s
st = input().lower()
print(find(st))