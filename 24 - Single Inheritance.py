# class Employee:     # Base Class/Parent Class
#     increment = 5000
#     no_of_leaves = 30

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
    
#     def printdetails(self):
#         print(f"Name is {self.name}, age is {self.age} and salary is {self.salary}.")

# class Developer(Employee):
#     pass

# emp = Employee("Ramesh", 34, 45000)
# dev = Developer("Naveen", 32, 35000)
# # print(emp.name)
# # emp.printdetails()
# # print(dev.name)
# # dev.printdetails()
# print(dev.increment)

# Write a program to print area of a rectangle and area of a square using single inheritance

# class Area:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Rectangle(Area):
#     def area_rectangle(self):
#         rec_area = self.length * self.width
#         print("Area of Rectangel is:", rec_area)

# class Square(Area):
#     def area_square(self):
#         sq_area = self.length * self.length
#         print("Area of Square is:", sq_area)

# # area_obj = Area(5,6)
# rect_obj = Rectangle(5,6)
# rect_obj.area_rectangle()
# square_obj = Square(7,7)
# square_obj.area_square()

class Area:
    def area_rectangle(self, length, width):
        rec_area = length * width
        print("Area of Rectangel is:", rec_area)
    
    def area_square(self, length):
        sq_area = length * length
        print("Area of Square is:", sq_area)

class Rectangle(Area):
    pass

class Square(Area):
    pass

# area_obj = Area(5,6)
rect_obj = Rectangle()
rect_obj.area_rectangle(5,6)
square_obj = Square()
square_obj.area_square(7)