class Maison:
    def  __init__(self, lenght):
         self.lenght = lenght
         self.height = 10
         self.nbWindows = lenght//3
         self.color = "white"

    def paint(self, color):
        self.color = color  


class Cabane(Maison):
     def  __init__(self):
          super().__init__(5)
          self.state = "délabrée"          

m1 = Maison(5)
m2 = Maison(18)
m3 = Cabane()

m1.paint("blue")

print(m1.color)
