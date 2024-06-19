#Lcm
import math
def Lcm(n):
    lcm = 1
    for i in range(1, n+1):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm
