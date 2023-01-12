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

    # Class methods used to change the instance variable of a class
    # @classmethod     # decorator
    # def change_increment(cls, amount):
    #     cls.increment = amount

#     @classmethod
#     def altconstructor(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printstatic():
#         print("This is a static method")

# emp1 = Employee("Ramesh", 23, 23000, 2000)
# emp2 = Employee.altconstructor("Naveen-25-25000-3000")
# print(emp1.name)
# print(emp2.name)
# print(emp2.age)