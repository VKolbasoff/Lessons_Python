class Restangle:
    x = 0
    y = 0
    widgt = 0
    hight = 0
    def __init__(self, x, y, widgt, hight, squa):
        self.x = x
        self.y = y
        self.widgt = widgt
        self.hight = hight
        self.squa = squa
    def __str__(self):
        return "Coordimates of the restangle: (" + str(self.x) + ";" + str(self.y) + ")" + "\nWidth:" + str(self.widgt)+ " " + "Hight:" + str(self.hight)
    def setsqr(self, squa):
        return self.widgt * self.hight


rest = Restangle(6, 10, 67, 48)

print(rest)
print()





