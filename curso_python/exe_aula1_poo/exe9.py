class Cachorro:
    especie = "Canis familiaris"

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"O cachorro: {self.nome} que tem {self.idade} anos de idade"

dog1 = Cachorro("Raika", 3)
dog2 = Cachorro("Tufão", 10)

print(f"A especie o cachorro é {Cachorro.especie}")

print(f"A especie de {dog1} é da especie {dog1.especie}")