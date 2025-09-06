#print (43 - 7)
#print (43 + 7)
#print (43 * 7)
#print (43 / 7)

#print("Hello World!")

vies = 255
#vies -= 1
print(vies)

if vies < 255:
    print("Dommage !")
    print ("Tu as perdu de la vie !")
else:
    print ("Bravo ! Tu n'as pas perdu de vie !")


for i in range (5):
    print(i)

while vies > 0:
    print ("Zacian utilise Gladius Maximus !")
    vies -= 100
    print ("C'est super éfficace !")

if vies <= 0:
    print ("Charmilly est mis K.O !")