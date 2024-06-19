string = input()
reversString = ''
for cha in string:
    reversString = cha + reversString
if string == reversString:
    print("palndrom")
else:
    print('not')