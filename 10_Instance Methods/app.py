# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,breed):
        self.name = name   # instance variables
        self.breed = breed # instance variables

    def bark(self):  # instance method 
        print(f"{self.name} is woofing!")

msg = Dog("Charlie","German Shepherd")
msg.bark()