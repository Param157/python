class Father:
    def showdetails(self):
        print("I am Father Class")


class Mother:
    def showdetails(self):
        print("I am Mother Class")

class Child(Mother, Father):
    pass

cobj = Child()
cobj.showdetails()