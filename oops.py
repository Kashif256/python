# OOPS (Object-Oriented Programming):
# OOPS is a programming approach that organizes code using
# classes and objects to make it reusable and easy to manage.


# Class:
# A class is a blueprint or template used to create objects.
# It contains attributes (data) and methods (functions).


# Example:

class Rectangle:
    length = 10
    breadth = 20

# Rectangle -> Class name
# length and breadth -> Attributes

class Student:

    def __init__(self):
        self.name = "Kash"
        self.age = 21

student1 = Student()

print(student1.name)
print(student1.age)


# __init__() → Constructor method.
# self → Refers to the current object.
# - Class → Blueprint.
# - Object → Actual instance of a class.
# - Attributes → Properties or data of an object.
# - Methods → Actions or functions performed by an object.


class Rectangle:
    def __init__(sanu):
        sanu.length = 10
        sanu.breadth = 20
react = Rectangle ()

print(react. length * react.breadth)  # o/p =>200
print(react. length) # o/p => 10
print(react. breadth) # o/p => 20

# paramaterised constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects with different values
#student1 = Student("Kashif", 21)
#student2 = Student("Sanu", 21)
reacting = Student("kashif", 21)
print(reacting.name)
#print(student1.name, student1.age)
#print(student2.name, student2.age)

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects with different values
student1 = Student("Kashif", 21)
student2 = Student("Sanu", 21)
print(student1.name, student1.age)
print(student2.name, student2.age)

#class Student → Create the class only once.
#student1 = Student("Kashif", 21) → First object.
#student2 = Student("Saniya", 20) → Second object.
#Both objects use the same constructor but have different values
     
print("-----------Class variable & instance variable")

# 1. Class Variable
# A class variable is a variable declared inside a class but outside the constructor (__init__). It is shared by all objects of that class.

# 2. Instance Variable
# An instance variable is a variable declared using self inside the constructor. Each object has its own separate value.

class Student:

    # Class variable
    college = "CAHCET"

    def __init__(self, name, age):

        # Instance variables
        self.name = name
        self.age = age


student1 = Student("Kashif", 21)
student2 = Student("Saniya", 20)

print(student1.college)
print(student2.college)

print(student1.name)
print(student2.name)


# second example

class circle:
    pi = 3.14
    def __init__(radiu, radius):
        radiu. radius = radius
circle1 = circle(5)
print(circle1.radius) # 5
print(circle.pi) # 3.14

# for changing class variable
# class variable name = new value
circle.pi = 3.1458
print(circle.pi) # 3.1458



    
    