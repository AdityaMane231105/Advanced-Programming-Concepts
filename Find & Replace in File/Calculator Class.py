class Calculator:
    def add(self, a=0, b=0, c=0, d=0):
        return a + b + c + d

calc = Calculator()

print("Add 2 numbers:", calc.add(5, 10))
print("Add 3 numbers:", calc.add(5, 10, 15))
print("Add 4 numbers:", calc.add(5, 10, 15, 20))

