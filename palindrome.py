# Faites un programme qui vérifie si un texte est un palindrome.
import unicodedata


def palindrome(phrase):
    phrase = ''.join(i.lower() for i in phrase if i.isalpha())
    phrase = unicodedata.normalize('NFD', phrase)
    phrase = ''.join(i for i in phrase if unicodedata.category(i) != 'Mn')
    if len(phrase) <= 1:
        return True
    if phrase[0] != phrase[-1]:
        return False
    return palindrome(phrase[1:-1])


c = palindrome('Ta bête te bat !')
print(c)

