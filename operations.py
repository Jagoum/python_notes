from math import pow

class Operations():
    """This is an object for performing mathemathical operations"""
    
    def __init__(self, num1):
        self.num1 = num1
        
    def add(self, num1):
        """This function is to add two numbers"""    
        return num1 + self.num1
    
    def subtract(self, num1):
        """This function is to get the difference of two numbers"""
        return num1 - self.num1
    
    def multiply(self, num1):
         """This function is to multiply two numbers"""
         return num1 * self
     
    def divide(self, num1):
        """This funciton is to divide the object by a number"""
        if num1 == 0:
            raise ZeroDivisionError("Cannot Divide number by zero. Division by zero is undefined")
        else:
            self.num1 / num1 
    
    def square(self):
        """This function is to square a number"""
        return pow(self.num1, 2)