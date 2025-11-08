#   fonction qui dessine la grille et préparation des cases où le joueur pourra jouer (values)
def draw_grid(values):
    print("   0       1       2   ")
    for j in range(3):
        for i in range(3):
            if i == 1:
                print(f"{j}  {values[j][0]}   |   {values[j][1]}   |   {values[j][2]}   ")
            else:
                print("       |       |       ")
        if j < 2:
            print(" ------+-------+-------")
values = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]
player_symbol = "X"

oPoints = 0
xPoints = 0

#   lancement du programme

while True:
    x = False
    o = False
    placeOccupe = False
    draw_grid(values)
    while True:
        answer = input(f"Vous êtes le joueur {player_symbol}, où voulez-vous jouer ? ")
        if answer == "quit":
            break
        try:
            numbers = answer.split(" ")
            if values[int(numbers[0])][int(numbers[1])] == " ":
                placeOccupe = False
            else:
                placeOccupe = True
            if placeOccupe:
                print(f"Cet endroit est déjà occupé par {values[int(numbers[0])][int(numbers[1])]}.")
                continue
            else:
                values[int(numbers[0])][int(numbers[1])] = player_symbol
                break
        except ValueError:
            print("Mauvaise position, réessaie !")
        except IndexError:
            print("Le chiffre doit être compris entre 0 et 2")
            # /////////////// DETECTION VICTOIRE OU MATCH NUL /////////////////
    if (
       values[0][0] == "X" and values[0][1] == "X" and values[0][2] == "X" or
       values[1][0] == "X" and values[1][1] == "X" and values[1][2] == "X" or
       values[2][0] == "X" and values[2][1] == "X" and values[2][2] == "X" or
       values[0][0] == "X" and values[1][0] == "X" and values[2][0] == "X" or
       values[1][1] == "X" and values[2][1] == "X" and values[0][1] == "X" or
       values[0][2] == "X" and values[1][2] == "X" and values[2][2] == "X" or
       values[0][0] == "X" and values[1][1] == "X" and values[2][2] == "X" or
       values[0][2] == "X" and values[1][1] == "X" and values[2][0] == "X"
       ):
        draw_grid(values)
        print("Le joueur X à gagné !")
        xPoints += 1
        print("Tu as ",xPoints," points contre ", oPoints,"!")
        rep1 = input("Voulez-vous recommencer ? oui/non: ")
        if rep1.lower() == "oui":
            print("Bonne chance!")
            values = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
            x = True
        elif rep1.lower() == "non":
            print("Au revoir!")
            quit()
    if (
       values[0][0] == "O" and values[0][1] == "O" and values[0][2] == "O" or
       values[1][0] == "O" and values[1][1] == "O" and values[1][2] == "O" or
       values[2][0] == "O" and values[2][1] == "O" and values[2][2] == "O" or
       values[0][0] == "O" and values[1][0] == "O" and values[2][0] == "O" or
       values[1][1] == "O" and values[2][1] == "O" and values[0][1] == "O" or
       values[0][2] == "O" and values[1][2] == "O" and values[2][2] == "O" or
       values[0][0] == "O" and values[1][1] == "O" and values[2][2] == "O" or
       values[0][2] == "O" and values[1][1] == "O" and values[2][0] == "O"
       ):
        draw_grid(values)
        print("Le joueur O à gagné !")
        oPoints += 1
        print("Tu as ",oPoints," points contre ", xPoints,"!")

        rep1 = input("Voulez-vous recommencer ? oui/non: ")
        if rep1.lower() == "oui":
            print("Bonne chance!")
            values = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
            x = True
        elif rep1.lower() == "non":
            print("Au revoir!")
            quit()
    if not (
            (" " in values[0] or
            " " in values[1] or
            " " in values[2] )
            ):
            draw_grid(values)
            matchNulVerif = input("Match nul! Voulez-vous recommencer ? oui/non ")
            if matchNulVerif.lower() == "oui":
                print("Bonne chance!")
                values = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
            elif matchNulVerif.lower() == "non":
                print("Au revoir!")
                quit()
            # //////////////// DETECTION S'IL VEUT VRAIMENT QUIT ///////////////
    if answer.lower() == "quit":
        rep = input("Êtes-vous sûr de vouloir quitter ? oui/non: ")
        if rep.lower() == "oui":
            print("Au revoir!")
            quit()
        elif rep.lower() == "non":
            continue
        # //////////////////// REENITIALISE LE JOUEUR //////////////////
    if x:
        player_symbol = "X"
    else:
        if player_symbol == "X":
            player_symbol = "O"
        else:
<<<<<<< HEAD
            player_symbol = "X"
=======
            player_symbol = "X"
>>>>>>> e7dd578929645c54c5f1738c8d3f30849091e11f
