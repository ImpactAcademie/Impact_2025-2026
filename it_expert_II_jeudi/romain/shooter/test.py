from random import randint

a_deviner =randint(1,100)
print("essaye de deviner un nombre entre 1 et 100")
reponse=0
while reponse!=a_deviner:
    reponse=int(input("essaye de trouver mon nombre:"))
    if reponse>a_deviner:
        print("mon nombre est plus petit")
    elif reponse<a_deviner:
        print("mon nombre est plus grand")
    else:
        print("NOOOOOOOOON, T'as gagné, je meuuuuurs")