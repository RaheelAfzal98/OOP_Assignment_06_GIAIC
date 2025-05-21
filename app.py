# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self,name,marks):
        self.fullname = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.fullname} and marks {self.marks}.")

std_data = Student("Raheel Afzal",98)
std_data.display()