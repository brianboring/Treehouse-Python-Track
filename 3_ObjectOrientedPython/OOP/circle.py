class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius): #must be named the same as the method you are trying to adjust (in this case radius)
        self.diameter = radius * 2


small = Circle(10)
print(small.diameter)
print(small.radius)

small.radius = 10 #would not be possible without @radius.setter because def radius is property of the class
print(small.diameter)