class Maison:
    def __init__(self, length):
        self.nbWindows = length//3
        self.length, self.heigth = length, 5


m1 = Maison(10)
m2 = Maison(25)
print(m1.heigth)
print(m2.nbWindows)