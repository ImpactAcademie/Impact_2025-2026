
def draw_grid(values):

    for j in range(3):

        for i in range(3):
            if i == 1:
                print(f'   {values[j][0]}   |   {values[j][1]}   |   {values[j][2]}   ' )
            else: 

             print('       |       |      ')

        if j < 2:

            print('-------+-------+-------')

values=[[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

player_symboel='X'

while True:

    draw_grid(values)
    while True:
            answer=input(f'vou etes le joueur {player_symboel} ,ou voulez-vous jouer')
    

    if answer=='quit ':
        break
    else:

                                                                           
            try:
                nubers=answer.split(' ')
                values[int(nubers[0])][int(nubers[1])]=player_symboel
                break
            except:
                print('mauvaise positiont')
                

    if player_symboel=='X':
        player_symboel='O'

    else:
        player_symboel='X'



