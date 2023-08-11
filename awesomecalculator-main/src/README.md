# Awesome Calculator
modified the existing code in the core.py file. The changes are listed below.
  Square Root, Improved Addition, Percentage Calculation
 #square root function
 import math
  class Calculator:
   def square_root(self,num):
     	return math.sqrt(num)
     	# The `Calculator` class now includes a `square_root` method that calculates 
     	result = calculator.square_root(121)
     	print(result) # output = 11
   
 #Improved Addition
 import math
  class Calculator:
  def Add(self,*value):     #to add all the numbers and return to the sum 
     return sum(value)
     result = calculator.add(15,25,20)
     ptint(result) 	#output = 60
     
 #  Percentage Calculation
 import math
   class Calculator:
    def percentage(self, value, percentage):
   	return (percentage/100)* value
   	result = calculator.percentage(200, 20)
       print(result)   # Output: 40.0
