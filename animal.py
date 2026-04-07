class Animal:
    def __init__(self, age, nom):
        self.age = age
        self.nom = nom
        self.cri = None

    def parle(self):
        return self.nom + " " + self.cri

class chat(Animal):
    def __init__(self, age, nom):
        super().__init__(age, nom)
        self.cri = "miaou"

    def ronronner(self):
        return " rrrrrrrrrrr "

class dog(Animal):
    def __init__(self, age, nom):
        super().__init__(age, nom)
        self.cri = "waf waf wouf"

class chaiench(dog, chat):
    def __init__(self, age, nom):
        super().__init__(age, nom)
        self.cri = "waf miaou wouf"



cici = chat(12, 'cici') #cherche dans class chat, puis on envoie via 'super' dans class animal les infos
bernard = dog(2, 'bernard')
zaurus = chaiench(5, 'zaurus')
#mixine
print(cici.parle())
# print(cici.parle())
# print(bernard.parle(), bernard.age)
#
# print(isinstance(bernard, dog))
# print(isinstance(cici, dog))