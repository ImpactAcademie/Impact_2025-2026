from random import randint

prix = randint(1,1000)
chances = 10

nb= int(input("Quel est le juste prix ? Tu as 10 chances "))

while nb != prix and chances != 0:
    if nb > prix:
        print("plus petit !")
        chances-=1
        nb= int(input("Quel est le juste prix ? N'oublie pas qu'il ne te reste plus que " + str(chances) + " chances :"))
    elif nb < prix:
        print("plus grand !")
        chances-=1
        nb= int(input("Quel est le juste prix ? N'oublie pas qu'il ne te reste plus que " + str(chances) + " chances :"))
if chances == 10:
    print("Tu as perdu !")
elif nb == prix:
    print("Tu as trouvé, bien joué !")