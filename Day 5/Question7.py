'''Minimum Number of Key Presses
George has a setup which includes a special keyboard and a monitor , that initially
displays 0. The special keyboard has 11 numeric keys (0,1,2,3,4,5,6,7,8,9,00). If he
presses 00, the previously displayed value will be multiplied by 100. Whereas, if he
presses any other numeric key, the previously displayed value will be firstly multiplied
by 10 and then the number on the key will be added to it
You are given a numeric string S. Your task is to help George find and return an
integer value, representing the minimum number of key presses to reach the number. Input Specification:
input: A numeric string s. representing the final number,
Output Specification:
Return an integer value, representing the minimum number of key presses to reach
the number.
Sample Input:
100
Sample Output:
2'''
def min_key_presses(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if s[i - j:i] != '0' and int(s[i - j:i]):
                dp[i] = min(dp[i], dp[i - j] + 1)
            if j >= 2 and s[i - j:i] == '00':
                dp[i] = min(dp[i], dp[i - j] + 1)
                return dp[n]
    return dp[n]
s = input()
print(min_key_presses(s))
