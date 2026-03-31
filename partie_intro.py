#Créer une variable a qui contient 'coucou'
from calendar import error

a = 'coucou'

#Créer une variable b qui contient un dict.
b = {}

#Ajouter a à b avec la clef 'c'
b['c'] = a

#Ajouter un dict à b avec la clef 'd'
b['d'] = {}

#Ajouter une list à 'd' avec la clef 'e'
b['d']['e'] = []

#Ajouter les données 2, None, 'hello' et 42 à 'e'
b['d']['e'] += 2, None, 'hello', 42
print(b['d']['e'])
print(b['d']['e'][2])

#Ajouter tous les nombres de 4 à 26 dans 'd' avec des clefs de 'a' à 'w'

lettres = list(map(chr, range(97, 120)))

for index, v in enumerate(range(4, 27, 1)):
    b['d'][lettres[index]] = v
print(b['d'])

#Ajouter une list qui contient toutes les valeurs de 'd' dans b avec la clef 'f'
f = []
for v in b['d'].values():
    f.append(v)
print(f)

#Ajouter toutes les valeurs de 'e' à 'f'
#Ajouter un try ... except pour éviter que l’erreur n’arrête pas le programme.
#faire un print de 'ouf' en cas d’erreur
print(b['d']['e'])

try :
    f += b['d']['e']
except :
    print('ouf')






