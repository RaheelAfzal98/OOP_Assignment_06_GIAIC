# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name    # public variable 
        self._salary = salary   # protected variable
        self.__ssn = ssn  # private variable

data_emp = Employee("Raheel",80000,"123-45-6789")
print("Name:", data_emp.name)
print("salary:", data_emp._salary)
#print(data_emp.__ssn)  # AttributeError: Can't access __ssn is a Private Varialbe not use directly
