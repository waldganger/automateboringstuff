#! python3

import sys, pyperclip

text = pyperclip.paste()

def bullet_add(texte):
    liste = texte.split('\n')
    print(liste)
    resultat = []
    for li in liste:
        start = "* "
        resultat.append(start + li)
    print(resultat)
    return '\n'.join(resultat)

pyperclip.copy(bullet_add(text))