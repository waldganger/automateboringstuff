spam = ['apples', 'bananas', 'tofu', 'cats']

def formater(liste):
    for i in range(len(liste) - 1):
        if i == len(liste) - 2:
            print(f'and {liste[i]}.')
            break
        print(liste[i], end=', ')

formater(spam)