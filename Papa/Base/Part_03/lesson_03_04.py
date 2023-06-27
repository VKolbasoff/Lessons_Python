from math import sqrt
class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def __str__(self):
        return "Coordimates: (" + str(self.x) + ";" + str(self.y) + ")"

p = Point(5, 5)
print(p.range(Point(0, 0)))
print(p.range(Point(3, 10)))
print(p)

class Auto:
    p = Point(0, 0)
    speed = 0
    def __init__(self, p = Point(0, 0), speed = 0):
        self.p = p
        self.speed = speed
    def setspeed(self, speed):
        self.speed = speed
    def gettime(self, endp):
        if self.speed != 0:
            return self.p.range(endp) / self.speed
        else:
            return -1

auto = Auto()
auto.setspeed(50)
print(auto.speed)
print(auto.gettime(Point(100, 100)))
auto.setspeed(0)
print(auto.gettime(Point(100, 100)))






