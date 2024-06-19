def HappyNumbers(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
    return False
n = int(input("Enter a number: "))
if HappyNumbers(n):
    s = "Happy Number" 
else:
    s = "Not a Happy Number"
print(f"{n} is a {s}")
#HappyNumbers(19) #True
#HappyNumbers(20) #False
#HappyNumbers(13) #True
