cmd = {
    "client": "bob",
    "products": [
        {"product": "apple", "unit_price": 1, "qt": 5},
        {"product": "sausage", "unit_price": 16.4, "qt": 72},
        {"product": "water in plastic bottle", "unit_price": 0.75, "qt": 12},
        {"product": "macbook pro", "unit_price": 2000.99, "qt": 1},
        {"product": "paper", "unit_price": 2, "qt": 3},
    ]
}
#calculer et afficher le total de la commande
produits = cmd['products']
prix = produits[0]['unit_price']
print("prix =", prix)

total_commande = 0
for i in produits:
    total_commande += i['unit_price']
print("total =", total_commande)

#→ idem mais ajoutez une tva de 20%
total_commande = 0
for i in produits:
    total_commande += i['unit_price']
    total_commande_tva = (total_commande * 0.20) + total_commande
print("total TVA =", total_commande_tva)

#idem mais la tva est à 5.5% pour les produits qui commencent par “a” ou “p”, 20% pour les autres.
for i in produits:
    if i['product'].startswith('a') or i['product'].startswith('p'):
        prix = (i['unit_price'] * 0.055) + i['unit_price']
        total_commande_tva += prix
    else:
        prix = (i['unit_price'] * 0.20) + i['unit_price']
        total_commande_tva += prix
print("prix tva 5 ou 20 =", total_commande_tva)

#idem mais il y a 17% de remise (sur le prix hors taxe) sur les produits qui ont un nombre de lettres paire dans leur nom.
total_commande_tv = 0
for i in produits:
    prix = i['unit_price']

    if len(i['product']) % 2 == 0:
        prix_remise = prix * (1- 0.17)

    if i['product'].startswith(('a', 'p')):
        prix_tva = (prix * 0.055) + prix

    else:
        prix_tva = (prix * 0.20) + prix
    total_commande_tv += prix_tva

    if len(i['product']) % 2 == 0:
        prix_remise = prix * (1- 0.17)

print("prix tva 5 ou 20, pair =", total_commande_tv)

cmd2 = {
    "client": "John Wish",
    "products": [
        {"product": "gros flingue", "unit_price": 1, "qt": 100},
        {"product": "grosse voiture", "unit_price": 1, "qt": 1},
        {"product": "petit chien", "unit_price": 1000, "qt": 0},
        {"product": "plus gros flingues", "unit_price": 2, "qt": 10},
        {"product": "costume blindé", "unit_price": 1, "qt": 3},
				{"product": "alcool divers", "unit_price": 12.5, "qt": 5}
    ]
}

produits = cmd2['products']
total_commande2 = 0
for i in produits:
    total_commande += i['unit_price']
print("total =", total_commande2)

#→ idem mais ajoutez une tva de 20%
total_commande2 = 0
for i in produits:
    total_commande2 += i['unit_price']
    total_commande_tva2 = (total_commande2 * 0.20) + total_commande2
print("total TVA =", total_commande_tva2)

#idem mais la tva est à 5.5% pour les produits qui commencent par “a” ou “p”, 20% pour les autres.
for i in produits:
    if i['product'].startswith('a') or i['product'].startswith('p'):
        prix = (i['unit_price'] * 0.055) + i['unit_price']
        total_commande_tva2 += prix
    else:
        prix = (i['unit_price'] * 0.20) + i['unit_price']
        total_commande_tva2 += prix
print("prix tva 5 ou 20 =", total_commande_tva2)

#idem mais il y a 17% de remise (sur le prix hors taxe) sur les produits qui ont un nombre de lettres paire dans leur nom.
total_commande_tv2 = 0
for i in produits:
    prix = i['unit_price']

    if len(i['product']) % 2 == 0:
        prix_remise = prix * (1- 0.17)

    if i['product'].startswith(('a', 'p')):
        prix_tva = (prix * 0.055) + prix

    else:
        prix_tva = (prix * 0.20) + prix
    total_commande_tv2 += prix_tva

    if len(i['product']) % 2 == 0:
        prix_remise = prix * (1- 0.17)

print("prix tva 5 ou 20, pair =", total_commande_tv2)