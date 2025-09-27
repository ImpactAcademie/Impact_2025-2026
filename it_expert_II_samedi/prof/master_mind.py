from random import choice

master_mind = []
for i in range(5):
    master_mind.append(choice(["r", "g", "b"]))
guess = []
comp = [None]*len(master_mind)

while comp.count("!") != len(master_mind):
    guess = input("Essaye: ")
    for i in range(len(guess)):
        if guess[i] == master_mind[i]:
            comp[i] = "!"
        elif guess[i] in master_mind:
            comp[i] = "~"
        else:
            comp[i] = "X"
    print(comp)