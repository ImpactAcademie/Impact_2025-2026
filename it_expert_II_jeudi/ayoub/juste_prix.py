from random import randint


juste_prix = randint(1, 100)
essai = 0

while True:
    prix_essai = int(input("Quel est le prix entre 1 et 100 ? "))
    essai += 1

    if prix_essai > juste_prix:
        print("Essai plus petit !")
    if prix_essai < juste_prix:
        print("Essai plus grand !")
    if prix_essai == juste_prix:
        print("Bien vus !")
        print("tu as trouvé en", essai, "essai.")
        break