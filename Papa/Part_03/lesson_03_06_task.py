class Auto:
    x = 0
    y = 0
    speed = 0
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self):
        print("Moving in to coordinates: " + str(self.x) + ":" + str(self.y))

class Mark(Auto):
    name = "0"
    def __init__(self,x, y, speed, name):
        Auto.__init__(self, x, y, speed)
        self.name = name
    def move(self):
        print(self.name + " Moving in to coordinates: " + str(self.x) + ":" + str(self.y))



p = Auto(10, 20, 5)
p.move()

p = Mark(4, 5, 3, "Audi")
p.move()

