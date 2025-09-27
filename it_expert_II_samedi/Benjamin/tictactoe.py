import time

def draw_grid(values):
    
    for j in range(3):
        for i in range(3):
            if i == 1:
                print(f"   {values[j][0]}   |   {values[j][1]}   |   {values[j][2]}   ")
            else:
                print("       |       |       ")
        if j < 2:
            print("-------+-------+-------")
values = [[" "," "," "],
          [" "," "," "],
          [" "," "," "]]
player_symbol = "X"
while True:
    draw_grid(values)
    answer = input(f"Vous êtes le joueur : {player_symbol}. Où voulez vous jouer ? ")
    while True: 
        if (answer) == "quit":
            break
        else:
            try:
                numbers = answer.split(";")
                values[int(numbers[0])][int(numbers[1])] = player_symbol
                break
            except:
                print("Mauvaise position, réessayez !")

    if player_symbol == "X":
        player_symbol = "O"
    else:
        player_symbol = "X"