from random import randint

piece = ('H', 'T')
jets = []

for i in range(100000):
    jets.append(piece[randint(0, 1)])

def counter(liste):
    memoire = [liste[0], liste[0]]          #initialisation de la mémoire
    count = 0

    stats = {
        piece[0] : 0,
        piece[1] : 0,
    }
    for el in liste:
        memoire[0] = el
        if el == memoire[1]:
            count += 1
            if count == 6:
                stats[el] += 1
        else:
            count = 0
        memoire[1] = memoire[0]
    stats[piece[0]] = (stats[piece[0]] / 100000) * 100
    stats[piece[1]] = (stats[piece[1]] / 100000) * 100
    return stats

resultats = counter(jets)

print(f"H: {resultats['H']}, T: {resultats['T']}")
