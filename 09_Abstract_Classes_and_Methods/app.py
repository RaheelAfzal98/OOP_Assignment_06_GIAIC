# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class shape(ABC): # Abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):   # Subclass
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
result = Rectangle(10,30)
print("Area of rectangle is:", result.area())