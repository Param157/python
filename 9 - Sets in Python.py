# Set is a data structure in python used to store multiple values in a single variable
# Set can't store duplicate value
# Set is mutable/changable
# Set is an unordered collection of data elements
# Set can contain multiple data types
# Set is an iterable

fruits = {"apple", "banana", "mango", "orange"}
# print(fruits)
# print(type(fruits))


# Set methods
# fruits.add("pineapple")     # add new element in set
# print(fruits)

# fruits.clear()
# print(fruits)

# x = fruits.copy()
# print(x)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# x = fruits1.difference(fruits2)
# print(x)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# fruits1.difference_update(fruits2)
# print(fruits1)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# x = fruits1.symmetric_difference(fruits2)
# print(x)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# x = fruits1.intersection(fruits2)
# print(x)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# fruits1.intersection_update(fruits2)
# print(fruits1)

# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# x = fruits1.union(fruits2)
# print(x)

# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana", "guava", "pineapple"}
# fruits1.update(fruits2)
# print(fruits1)

# fruits.remove("apple")
# print(fruits)


# fruits.discard("pineapple")
# print(fruits)


# fruits1 = {"apple", "banana", "mango", "orange"}
# fruits2 = {"apple", "banana"}
# x = fruits1.issuperset(fruits2)
# print(x)


# fruits1 = {"apple", "banana"}
# fruits2 = {"apple", "banana", "mango", "orange"}
# x = fruits1.issubset(fruits2)
# print(x)

# fruits1 = {"apple", "banana"}
# fruits2 = {"mango", "orange"}
# x = fruits1.isdisjoint(fruits2)
# print(x)