nombre_a_deviner = 37

nombre_essai = int(input("quel est ton nombre: "))

if nombre_essai > nombre_a_deviner:
    print("plus petit")
if nombre_essai < nombre_a_deviner:
    print("plus grand")
