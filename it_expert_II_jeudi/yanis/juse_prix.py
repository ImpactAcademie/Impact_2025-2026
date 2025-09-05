from random import randint


juste_prix = randint(1, 1000)
essai = 0

while True: 
    prix_essai = int(input("quel est le prix entre 1 et 1000"))
    essai +=1

    if prix_essai > juste_prix:
        print("plus petit")
    if prix_essai < juste_prix:
        print("plus grand")
    if prix_essai == juste_prix:
        print("bien joué!")
        print("tu as trouvé en", essai, "essais")
        break