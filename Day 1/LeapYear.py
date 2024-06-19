a = int(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
count = 0
for a in range(1850 , 2025):
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        count += 1
print(count)