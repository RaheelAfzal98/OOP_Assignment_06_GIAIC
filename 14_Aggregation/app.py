# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Employee: {self.name}")

class Department:
    def __init__(self,dept_name,employee):
        self.dept_name = dept_name
        self.employee = employee   # Aggregation

    def show(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()

emp = Employee("Raheel Afzal")   # Create an Employee independently
dept = Department("IT", emp)    # Department has a reference to the Employee

dept.show() 

