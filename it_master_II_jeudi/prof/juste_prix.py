from random import randint


nombre_a_deviner = randint(1, 100)

while True:
    nombre_essai = int(input("Devine un nombre entre 1 et 100: "))
    
    if nombre_essai < nombre_a_deviner:
        print("Plus grand")
    elif nombre_essai > nombre_a_deviner:
        print("Plus petit")
    else:
        print("Bien joué")
        break
