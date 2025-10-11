import random
from colorama import Style, Fore, init
init()
pPC = 0
pJ = 0
choixJeu = ["pierre", "papier", "ciseaux"]
continuer=True


while continuer:
  choix = input(Fore.LIGHTMAGENTA_EX + "Pierre papier ciseaux " + Style.RESET_ALL)
  if choix.lower() == "quit":
    quit()
  while not choix.lower() in choixJeu:
    if choix.lower() == "quit":
      quit()
    print(Fore.RED + "Réponse invalide...")
    choix = input(Fore.LIGHTMAGENTA_EX + "Pierre papier ciseaux " + Style.RESET_ALL)

  choixPC = random.choice(choixJeu)
  print(f"PC: {choixPC}")
  
  if choixPC == choix:
    print("Égalité!")

  if (choix == "pierre" and choixPC == "ciseaux" or
      choix == "ciseaux" and choixPC == "papier" or
      choix == "papier" and choixPC == "pierre"
    ):
    pJ += 1
    print("Tu l'as battu! +1 point")

  elif (
      choixPC == "pierre" and choix == "ciseaux" or
      choixPC == "ciseaux" and choix == "papier" or
      choixPC == "papier" and choix == "pierre"
      ):
    pPC += 1
    print("Il t'as battu... +1 point pour PC")
  print(f"Joueur: {pJ}, PC: {pPC}")

  rep = input(f"Voulez-vous continuer ?{Fore.LIGHTMAGENTA_EX} oui/non {Style.RESET_ALL}")

  while  not rep.lower() in ("non","oui"):
    print("Réponds par oui ou non")
    rep = input(f"Voulez-vous continuer ?{Fore.LIGHTMAGENTA_EX} oui/non {Style.RESET_ALL}")

  continuer = rep.lower() == "oui"
