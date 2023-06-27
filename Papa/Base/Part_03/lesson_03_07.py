from abc import ABC, abstractmethod
class Shape(ABC):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print(str(self.x) + ":" + str(self.y))

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    r = 0
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print("Draw Circle " + str(self.x) + ":" + str(self.y))

class Restangle(Shape):
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print("Draw Restangle " + str(self.x) + ":" + str(self.y) + ":" + str(self.w) + ":" + str(self.h))

#s = Shape(7, 8)
#s.draw()

c = Circle(10, 20, 5)
c.draw()

r = Restangle(30, 50, 30, 20)
r.w = 35
r.draw()

#s.printXY()
#c.printXY()
