# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:   # Engine class
    def __init__(self,horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is starting..."
    
class Car:  # Car class using composition
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        return f'{self.brand} {self.engine.start()}'

engine1 = Engine(150)
car1 = Car('Toyota',engine1)
print(car1.start_car())