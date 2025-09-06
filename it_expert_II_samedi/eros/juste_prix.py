
from random import randint

nombre_a_deviner =  randint(1,100)

nombre_essai=int(input('Quel est ton nombre entre 1 et 100'))

while nombre_essai != nombre_a_deviner:

    if nombre_essai > nombre_a_deviner:
        

        print('plus petit')


    if nombre_essai < nombre_a_deviner:

        print('plus grand')

    nombre_essai=int(input('Quel est ton nombre '))

print('bien joué')             