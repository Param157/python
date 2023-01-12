class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    def area(self):
        a=pow(self.side1, 2)
        print('Area of Square: ', a)
