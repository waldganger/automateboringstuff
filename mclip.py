#! python3

import sys, pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print("mcplip usage: mclip.py [mot-clé]")
    sys.exit()

mot_cle = sys.argv[1]

if mot_cle in TEXT:
    pyperclip.copy(TEXT[mot_cle])
    print(f"Texte pour {mot_cle} : {TEXT[mot_cle]} copié dans le presse-papier")
else:
    print(f"{mot_cle} non présent dans la KB.")