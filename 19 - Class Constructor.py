# Constructor is a function that define the properties of an object.
# Constructor automatically call when object created

class Employee:
    no_of_leaves = 30
    increment = 5000

    #Creating a constructor
    def __init__(self, name, age, salary, increment):
        self.name = name
        self.age = age
        self.salary = salary
        self.increment = increment

emp1 = Employee("Ramesh", 23, 23000, 2000)
emp2 = Employee("Naveen", 25, 25000, 3000)

print(emp1.name)
print(emp1.no_of_leaves)
print(emp1.increment)

print(Employee.__dict__)
print(emp1.__dict__)