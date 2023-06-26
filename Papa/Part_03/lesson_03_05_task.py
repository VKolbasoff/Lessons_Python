class Restangle:
    __x = 0
    __y = 0
    __widgt = 0
    __hight = 0

    def __init__(self, x, y, widgt, hight):
        self.__x = x
        self.__y = y
        self.__widgt = widgt
        self.__hight = hight

    def __str__(self):
        return "Coordimates of the restangle: (" + str(self.__x) + ";" + str(self.__y) + ")" + "\nWidth:" + str(
            self.__widgt) + " " + "Hight:" + str(self.__hight)

    def sqare(self):
        return self.__widgt * self.__hight

    def per(self):
        return self.__widgt * 2 + self.__hight * 2

    def getY(self):
        return self.__y
    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y

rest = Restangle(6, 10, 10, 20)

print(rest)
print(rest.sqare())
print(rest.per())



