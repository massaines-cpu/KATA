#Faire un programme en python qui trouve le nombre mystère en jouant le moins de coups possible.
from random import choice


mystere = choice(range(0, 123, 1))
print(mystere)
def jeu(i):
    if i == mystere:
        return "bravo"
    elif i > mystere:
        return "c\'est moins"
    else:
        return "c\'est plus"

min = 0
max = 123
while True:
    # joueur choisi un nombre
    i = int((min + max)/2)
    # test
    test = jeu(i)
    print(i, test)
    # en fonction de la reponse
    if test == 'bravo':
        break
    # modifie son nombre
    elif test == 'c\'est moins':
        max = i - 1
    else:
        min = i + 1

