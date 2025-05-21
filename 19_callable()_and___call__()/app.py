# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,number):
        return number * self.factor
    
multi = Multiplier(6)  # Create object

print(callable(multi))   # Test if object is callable   # True

print(multi(15))    # Call object like a function