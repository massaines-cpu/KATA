from calendar import error

compte = 0.0

#Créer une fonction operation(n) qui modifie la valeur de compte en ajoutant n

def operation(n):
    global compte
    if (compte + n) < 0:
        erreur = Exception('marre')
        raise erreur
    compte += n

# def operation(n):
#     calcul = compte + n
#     if calcul - n < 0 :
#         erreur = Exception('pas assez de sous')
#         raise erreur
#     return calcul

#Faire une opération à +100.
operation(100)

#Faire une opération à -30
operation(-30)


try:
    operation(-100)
except Exception as e:
        print('pauvre')


