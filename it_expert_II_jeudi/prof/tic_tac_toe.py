def draw_grid(values):
    for j in range(3):
        for i in range(3):
            if i != 1:
                print("       |       |       ")
            else:
                print(f"   {values[j][0]}   |   {values[j][1]}   |   {values[j][2]}   ")
        if j < 2:
            print("-------+-------+-------")
        
    

values = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]
player_symbol = "X"
victory = False
while not victory:
    draw_grid(values)
    while True:
        try:
            answer = input(f"Vous êtes le joueur {player_symbol} ou voulez-vous jouer ? ").split(" ")
            values[int(answer[0])][int(answer[1])] = player_symbol
            break
        except:
            print("Mauvaise position, réessayez")
    if player_symbol == "X":
        player_symbol = "O"
    else:
        player_symbol = "X"