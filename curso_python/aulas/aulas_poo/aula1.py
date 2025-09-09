class Cachorro:
    especie = "Canis lupus familiaris"
    def __init__(self, nome, raca, idade): #Metodo Construtor
        self.nome = nome
        self.raca = raca
        self.idade = idade
# auau = Cachorro()
# print(auau.especie)

def _str_(self):
    return f"Especie: {self.especie}\nNome: {self.nome}\nRaca: {self.raca}\nIdade: {self.idade}"

def latir(self):
    print("Au au au")

def correr(self, metros):
    print(f"{self.nome} correu {metros}m")


doguinho01 = Cachorro("Rex", "Caramelo",2)
print(doguinho01)
print(doguinho01.especie, doguinho01.nome, doguinho01.raca, doguinho01.idade, sep="\n")
print("_______________________________________")
print(_str_(doguinho01))

class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.operacoes = []
    
    def __str__(self):
        return f"Conta nº {self.numero_conta} do titular {self.nome} com saldo {self.saldo}"
    
    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente, vai trabalhar!")
        else:
            self.saldo -= valor
            self.operacoes.append(["saque", valor])
    
    def deposito(self, valor):
        self.saldo += valor

# conta1 = ContaBancaria("Frederico", 34141412)
# conta2 = ContaBancaria("Gleibson" 1463454252, 500000)

# print(conta1)
# print(conta2)