nombre_a_deviner = 37

nombre_essai = int(input("Quel est ton nombre: 3"))
while nombre_essai != nombre_a_deviner:
    if nombre_essai > nombre_a_deviner:
        print("plus petit")
    if nombre_essai < nombre_a_deviner:
        print("plus grand")
    nombre_essai = int(input("Quel est ton nombre: "))

        print("NAAAAAN AREH")
