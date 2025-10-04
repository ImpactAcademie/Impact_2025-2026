maList = []
for i in range(10):
    num = int(input("Donnez un chiffre/nombre au hasard: "))
    maList.append(num)

print("voici votre liste de nombre :", maList)

maxVal = max(maList)
print("Le nombre le plus grand de votre liste est", maxVal)