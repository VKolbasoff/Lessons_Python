class Restangle:
    x = 0
    y = 0
    widgt = 0
    hight = 0

    def __init__(self, x, y, widgt, hight):
        self.x = x
        self.y = y
        self.widgt = widgt
        self.hight = hight

    def __str__(self):
        return "Coordimates of the restangle: (" + str(self.x) + ";" + str(self.y) + ")" + "\nWidth:" + str(
            self.widgt) + " " + "Hight:" + str(self.hight)

    def sqare(self):
        return self.widgt * self.hight

    def per(self):
        return self.widgt * 2 + self.hight * 2


rest = Restangle(6, 10, 10, 20)

print(rest)
print(rest.sqare())
print(rest.per())


