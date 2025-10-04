class House :
    def __init__(self,length):
        self.length=length
        self.height=10
        self.nbWindows=length//3
        self.couleur='white'

    def paint(self,couleur):
        self.couleur=couleur
        

class Cabane(House):
    def __init__(self):
        super().__init__(5)
        self.state=['nul','petite']


m1=House(15)
m2=House(169)
m3=Cabane()
m1.paint('red')


print(m1.nbWindows)
print(m2.nbWindows)
print(m3.state)
print(m1.couleur)







