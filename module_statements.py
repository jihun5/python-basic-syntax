class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self, a):
        self.result += a 
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a
    def divide(self, a):
        self.result /= a        

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b 
# Calculator.plus(10)
# print(Calculator.result)
# Calculator.minus(5)
# print(Calculator.result)