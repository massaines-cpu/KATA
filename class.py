''' Créer la classe Dictionary qui permet de faire fonctionner le code suivant'''

class Dictionary:
    def __init__(self):
        self.data = {}

    def newentry(self, name, definition):
        self.data[name] = definition

    def look(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return f'can\'t find entry for {name}'



d = Dictionary()
d.newentry('Yacine', 'gentil')
print(d.look('Yacine'))
#a fruit that grows on trees
print(d.look('Banana'))
#can't find entry for banana