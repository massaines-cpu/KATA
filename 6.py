import random, string
from random import randint
from string import ascii_lowercase


#Faire un tableau f qui contient 676 str.
# Chaque str doit être un groupe de 2 lettres minuscules
# et chaque groupe doit être différent.
lettres = random.choices(list(map(chr, range(97, 123))), k=1352)
f = []
for i in range(0, len(lettres), 2):
    paire = lettres[i] + lettres[i+1]
    f.append(paire)
print('len f:',len(f))
print('f:', f)

#Créer f en une seule ligne de code.
f = [str(i) for i in f]
print('f en une ligne:', f)

#Créer g → même chose que f mais avec 3 lettres minuscules.
g = []
for i in range(0, len(lettres), 2):
    paire = lettres[i] + lettres[i+1] + lettres[i+1]
    g.append(paire)
print('g:', g)
print('len g :', len(g))

#Créer un dictionnaire h qui utilise les valeurs de g comme clef et des valeurs aléatoires entre 2 et 12.

def convertir_liste(liste):
    dictionnaire = {liste[i]: randint(2,12) for i in range(0, len(liste), 1)}
    return dictionnaire

h = convertir_liste(g)
print('h:', h)

#Créer h en une seule ligne de code et l’afficher
h = {k : v for k, v in h.items()}
print('h en une ligne:', h)

#Faire un print de la moyenne des valeurs de h.
# Exemple (si vous êtes très loin de 7 c’est qu’il y a un problème) :

somme_valeur_h = sum(h.values())
nombre_valeur_h = len(h.values())

moyenne = somme_valeur_h/nombre_valeur_h
print('moyenne:', moyenne)