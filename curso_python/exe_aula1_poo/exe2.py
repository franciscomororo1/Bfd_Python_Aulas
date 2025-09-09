class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} anos"
    
    def apresentar(self):
        return f"Olá meu nome é {self.nome} e tenho {self.idade} anos"

pessoa1 = Pessoa("Francisco Mororó", 42)
print(pessoa1.apresentar())
