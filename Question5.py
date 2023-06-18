# Inheritance is basically enable the option to use multilevel properties from different Classes.
#   There are 5 types of inheritance.

#Example 1 - Single Inheritance

class single_class1():
    def single_func1(self):
        print("This is Function 1")
class single_class2(single_class1):
    def single_func2(self):
        print("This is func 2")

a= single_class2()
a.single_func1()

#Example 2 - Multilevel Inheritance 

class multilevel_class1:
    def multilevel_func1(self):
        print("this is func 1")

class multilevel_class2(multilevel_class1):
    def multilevel_func2(self):
        print("This is func 2")

class multilevel_class3(multilevel_class2):
    def multilevel_func3(self):
        print("This is func 3")

multilevel_obj = multilevel_class3()
multilevel_obj.multilevel_func2()

# Example 3 - Multiple Inheritance

class multiple_class1:
    def multiple_func1(self):
        print("this is func 1")

class multiple_class2:
    def multiple_func2(self):
        print("This is func 2")

class multiple_class3(multiple_class1,multiple_class2):
    def multiple_func3(self):
        print("This is func 3")

multiple_obj = multiple_class3()
multiple_obj.multiple_func2()
multiple_obj.multiple_func1()


#Example 4 - Hierarchical Inheritance


class Hierarchical_class1:
    def Hierarchical_func1(self):
        print("this is func 1")

class Hierarchical_class2(Hierarchical_class1):
    def Hierarchical_func2(self):
        print("This is func 2")

class Hierarchical_class3(Hierarchical_class1):
    def Hierarchical_func3(self):
        print("This is func 3")

Hierarchical_obj = Hierarchical_class3()
Hierarchical_obj.Hierarchical_func1()

#Example 5 - Hybrid Inheritance 

# Creating a Base class named University:
class University:
  def __init__(self):
    print("Contructor of the Base class")
    # Initializing a class variable named univ to store university name:
    self.univ = "MIT"
  def display(self):  # Method to print the University Name:
    print(f"The University name is: {self.univ}")

# 1st Derived or Child Class of University Class:
class Course(University):
  def __init__(self):
    # using "super" keyword to access members of the parent class having same name:
    print("Constructor of the Child Class 1 of Class University")
    University.__init__(self)
    self.course = "CSE"
  def display(self):  # Method to print the Course Name:
    # using "super" keyword to access display method defined in the parent class:
    print(f"The Course name is: {self.course}")
    University.display(self)

# 2nd Derived or Child Class of University Class:
class Branch(University):
  def __init__(self):
    print("Constructor of the Child Class 2 of Class University")
    self.branch = "Data Science"
  def display(self):  # Method to print the Branch Name:
    print(f"The Branch name is: {self.branch}")

# Derived or Child Class of Class Course and Branch:
class Student(Course, Branch):
  def __init__(self):
    print("Constructor of Child class of Course and Branch is called")
    self.name = "Tonny"
    Branch.__init__(self)
    Course.__init__(self)
  def display(self):
    print(f"The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)

# Object Instantiation:
ob = Student()  # Object named ob of the class Student.
print()
ob.display()    # Calling the display method of Student class.