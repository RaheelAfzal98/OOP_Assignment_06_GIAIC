# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total NO. Of Objects Created: {cls.count}.")


obj1 = Counter()
Obj2 = Counter()
Counter.display_count()