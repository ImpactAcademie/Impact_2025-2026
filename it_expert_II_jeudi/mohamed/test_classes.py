class Maison:
    def __init__(self, length):
        self.nbWindows = length//3
        self.lenght, self.height = length, 5

class Cabane(Maison):
    def __init__(self):
        super().__init__(5)
        self.nbWindows = 0

m1 = Maison(10)
m2 = Maison(25)
m3 = Cabane()

print(m1.nbWindows)
print(m2.nbWindows)
print(m3.nbWindows)