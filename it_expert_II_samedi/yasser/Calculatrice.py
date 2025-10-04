reponse = "o"
while reponse == "O" or reponse == "o":
  nb1 = int(input("Entre le premier nombre: "))
  nb2 = int(input("Entre le second nombre: "))
  print("======================")

  somme = nb1+nb2
  print("Voici la somme " + str(somme))

  prdt = nb1*nb2
  print("voici le produit " + str(prdt))

  dif = nb1-nb2
  print("voici la différence " + str(dif))

  qtn = nb1/nb2
  print("voici le quotient " + str(qtn))

  print("///////////////////////////")

  n1 = int(input("Entre le premier nombre: "))
  ope = input("Quelle opération (+, -, * ou /): ")
  n2 = int(input("Entre le second nombre: "))

  if ope == "+":
    print(f"Voici la somme {n1+n2}")
  elif ope == "*":
      print(f"voici le produit {n1*n2}")
  elif ope == "-":
      print(f"voici la différence {n1-n2}")
  elif ope == "/":
      print(f"voici le quotient {n1/n2}")
  reponse = input("Voulez-vous continuer (O/N)? ")