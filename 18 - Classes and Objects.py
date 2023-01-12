# OOPs is based on concept of objects... which can contain data and code. Data in form of Fields (often knows as attributes and properties) and Code in form of procedures (often known of methods).

class Employee:         # Creating a class
    no_of_leaves = 30   # Instance variable of a class
    increment = 5000

emp1 = Employee()       # Creating a object
emp2 = Employee()

print(emp1.no_of_leaves)
print(emp1.increment)

emp1.name = "Ramesh"
emp1.age = 32
emp1.salary = 23000

emp2.name = "Naveen"
emp2.age = 30
emp2.salary = 25000

# The object of a class can access all the properties of that class.

print(emp1.name)
print(emp2.salary)