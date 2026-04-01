#On demande 2 nombres à l'utilisateur (X et Y), puis on affiche des # pour réaliser une grille de X colonnes par Y lignes.

x = int(input('entrez un nombre X:'))
y = int(input('entrez un nombre Y:'))

for _ in range(y):
    print('#'* x)

