# Dictionary is a data structure in python used to store multiple values in a single variable
# Dictionary stores data in Key:Value pair
# Keys should be unique and value can be duplicate
# Dictionary is mutable/changable
# Dictionary is an unordered collection of data elements
# Dictionary can contain multiple data types
# Dictionary is an iterable

prices = {"shirt":600,"shoes":800, "wallet":600}
# print(prices)
# print(type(prices))

# print(prices["shirt"])    # Print value of a key

# prices["shirt"] = 1000    # Update a value of a key
# print(prices)

# prices["bracelet"] = 1000   # Add a new key with value
# print(prices)

# prices.clear()
# print(prices)

# print(prices.copy())

# print(prices.get("shirt"))
# print(prices.items())
# print(prices.keys())
# print(prices.values())

# prices.pop("shirt")
# print(prices)

# prices.popitem()
# print(prices)

# x = {'android':5000,'iphone':20000}
# prices.update(x)
# print(prices)


# The fromkeys() method returns a dictionary with the specified keys and the specified value.

# x = ("shirt","shoes", "wallet")
# y = 0
# prices = dict.fromkeys(x,y)
# print(prices)

# The setdefault() method returns the value of the item with the specified key.
# prices = {"shirt":600, "wallet":600}
# prices.setdefault("shoes",850)
# # print(x)
# print(prices["shoes"])
# print(prices)