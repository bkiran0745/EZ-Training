if __name__ == '__main__':
    s = input()
def islnum1(s):
    for i in s:
        if i.isalnum():
            return True
    return False  
def isalpha1(s):
    for i in s:
        if i.isalpha():
            return True
    return False
def isdigit1(s):
    for i in s:
        if i.isdigit():
            return True
    return False

def islower1(s):
    for i in s:
        if i.islower():
            return True
    return False
def isupper1(s):
    for i in s:
        if i.isupper():
            return True
    return False
    
if islnum1(s):
    print("True")
else:
    print("False")
if isalpha1(s):
    print("True")
else:
    print("False")
if isdigit1(s):
    print("True")
else:
    print("False")
if islower1(s):
    print("True")
else:
    print("False")
if isupper1(s):
    print("True")
else:
    print("False")