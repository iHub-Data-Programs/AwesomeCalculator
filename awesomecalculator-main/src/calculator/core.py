import math
class Calculator:
    def __init__(self):
        pass

    def Add(self,*numbers):
        return math.sum(numbers)

    def Substract(self, value1, value2):
        return value1 - value2

    def Multiply(self, value1, value2):
        return value1 * value2

    def Divide(self, value1, value2):
        return value1 / value2
    def square_root(self,num):
        return math.sqrt(num)
    def percentage(self,num,percentage):
        return ((percentage * value)/100)