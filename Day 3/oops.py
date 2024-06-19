class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

obj1 = Calculator
print(obj1.add(4,9))
obj2 = Calculator
print(obj2.mul(9,32))
obj3 = Calculator
ans = obj3.div(10,12)
print(ans)