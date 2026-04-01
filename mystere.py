from random import *

#Le programme choisi un nombre au hasard entre 0 et 123, le nombre mystère.

choix_mystere = choice(range(0, 123, 1))
print(choix_mystere)

while not False:
    # Il demande à l'utilisateur de le deviner.
    # L'utilisateur choisit un nombre.
    texte = int(input('devine mon nombre:'))
    # Le programme compare le nombre avec le nombre mystère

    if texte == choix_mystere:
        print('bravo')
        break
    elif texte > choix_mystere:
        print('c\'est moins')
    else:
        print('c\'est plus')
