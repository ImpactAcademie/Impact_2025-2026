liste = [-10, -4, -9, -5, -10, -87, -18]

def minimum(liste):
    minimum = liste[0]
    for x in liste:
        if x < minimum:
            minimum = x
    return minimum


new_list = []
while len(liste) > 0:
    m = minimum(liste)
    new_list.append(m)
    liste.remove(m)


print(new_list)