class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def __test(self):
        print("Privite method.")
    def runPrivite(self):
        self.__test()


p = Point(10 ,10)
print(p.getX())
print(p.getY())
p.setX(20)
p.setY(15)
print(p.getX())
print(p.getY())

p.runPrivite()


