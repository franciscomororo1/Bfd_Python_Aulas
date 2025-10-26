class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def som(self):
        print("som indefinido")

class Cachorro(Animal):
    def som(self):
        print("au au")

class Mamifero:
    def __init__(self, idade, habitat, som):
        self.idade = idade
        self.habitat = habitat
        self.som = som
        self.prole = "gestação"
        self.alimentacao_infantil = "leite"
    
    def som(som):
        print(som)

class Morcego(Mamifero):
    def __init__(self, idade, habitat, som, locomocao = "vôo"):
        super().__init__(idade, habitat, som)
        self.locomocao = locomocao

zubat = Morcego(1, "laje", "assobio")

print(zubat.idade)
print(zubat.habitat)
print(zubat.som)
print(zubat.locomocao)
print(zubat.prole)
print(zubat.alimentacao_infantil)

# dog1 = Cachorro("Raika", 3)
# print(dog1.nome)
# print(dog1.idade)
# dog1.som()