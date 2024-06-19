s = input()
list = ['a','e','i','o','u']
count = 0
for i in s:
    if i in list:
        count += 1
print(count)