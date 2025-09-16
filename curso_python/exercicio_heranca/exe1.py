class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        
    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} anos, endereço: {self.endereco}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, cargo, salario):
        super().__init__(nome, idade, endereco)
        self.cargo = cargo
        self.salario = salario

pessoa1 = Funcionario("Francisco", "42", "R- Maciel monteiro, 02", "Analista", 5000)
print(pessoa1)
print(f"Cargo: {pessoa1.cargo} Salário: {pessoa1.salario}")
