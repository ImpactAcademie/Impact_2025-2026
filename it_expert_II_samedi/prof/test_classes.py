class Maison:
    def __init__(self, length):
        self.length = length
        self.height = 10
        self.nbWindows = length//3
        self.color = "white"

    def paint(self, color):
        self.color = color


class Cabane(Maison):
    def __init__(self):
        super().__init__(5)
        self.state = "délabrée"

m1 = Maison(5)
m2 = Maison(18)
m3 = Cabane()

m1.paint("red")

print(m1.color)

m3.paint()