# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self,brand):
        self.brand = brand # Public Variable

    def start(self):
        print(f"{self.brand} is Starting...") 

my_car = Car("Rolls Royce")
print(f"Car Brand: {my_car.brand}") # Public Variable
my_car.start() # Public Method