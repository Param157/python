class Grandfather():
    no_of_leaves = 30

class Father(Grandfather):
    salary = 45000

class Child(Father):
    incentive = 10000

gobj = Grandfather()
fobj = Father()
cobj = Child()

print(cobj.no_of_leaves)
print(cobj.salary)
print(cobj.incentive)