class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} anos"

pessoa1 = Pessoa("Francisco", 42)
pessoa2 = Pessoa("Bruna", 35)    

print(pessoa1)
print(pessoa2)



