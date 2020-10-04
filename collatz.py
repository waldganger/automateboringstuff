import sys

def collatz(number):
    if number == 1:
        return number
    elif not number % 2:
        even = number // 2
        print(even)
        return collatz(even)
    else:
        odd = 3 * number + 1
        print(odd)
        return collatz(odd)

while True:
    try:
        num = int(input("Entrez le nombre de départ de la séquence de Collatz.\n"))
        collatz(num)
        break
    except ValueError:
        print("Entrez un nombre entier svp.")   