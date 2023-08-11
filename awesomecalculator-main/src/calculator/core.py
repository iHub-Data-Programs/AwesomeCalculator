import math

class Calculator:
    def __init__(self):
        pass

    # This function can add unlimited any of number
    def Add_(self, *values):
        return math.sum(values)

    def Substract(self, value1, value2):
        return value1 - value2

    def Multiply(self, value1, value2):
        return value1 * value2

    def Divide(self, value1, value2):
        return value1 / value2
        
    # This function will calculate the square-root of the given number and return the result
    def Square_root(self, num):
        return math.sqrt(num)
        
    # This function will calculate the percentage of the given value and return the result
    def Percentage(self, value, percentage):
    	return (value*percentage)/100
    	
 

