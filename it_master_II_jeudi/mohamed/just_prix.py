from random import randint


juste_prix = randint(1, 1000)

while True:
    prix_essai = int(input("Quel est le prix entre 1 et 1000 ? "))

    if prix_essai > juste_prix:
        print("Plus petit")
    if prix_essai < juste_prix:
        print("Plus grand")
    if prix_essai == juste_prix:
        print("bien joué !")
        print("Tu as trouvé en", essai, "essais.")
        break