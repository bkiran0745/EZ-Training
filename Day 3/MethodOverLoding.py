class Calculator:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total
calculator = Calculator()
print(calculator.add(1,2))
print(calculator.add(1,2,3,4,5))