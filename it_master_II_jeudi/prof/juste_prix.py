from random import randint


juste_prix = randint(1, 1000)
essai = 0

while True:
    prix_essai = int(input("Quel est le prix entre 1 et 1000 ? "))
    essai += 1

    if prix_essai > juste_prix:
        print("Plus petit")
    if prix_essai < juste_prix:
        print("Plus grand")
    if prix_essai == juste_prix:
        print("Bien joué !")
        print("Tu as trouvé en", essai, "essais.")
        break