# class Employee:
#     no_of_leaves = 30
#     increment = 5000

#     #Creating a constructor
#     def __init__(self, name, age, salary, increment):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.increment = increment

#     def print_details(self):
#         print(f"The name is {self.name} age is {self.age} salary is {self.salary} and increment is {self.increment}")

#     # Class methods used to change the instance variable of a class
#     @classmethod     # decorator
#     def change_increment(cls, amount):
#         cls.increment = amount

#     @staticmethod
#     def printstatic():
#         print("This is a static method")

# emp1 = Employee("Ramesh", 23, 23000, 2000)
# emp2 = Employee("Naveen", 25, 25000, 3000)
# Employee.change_increment(10000)
# print(Employee.increment)
# emp1.printstatic()