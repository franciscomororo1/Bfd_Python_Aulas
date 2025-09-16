class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
       
    def __str__(self):
        return f"Titular: {self.titular} Saldo: {self.saldo}"
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Foi depositado {valor} reais na sua conta")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

conta1 = ContaBancaria("Rodolfo", 1000)

if conta1.saque(300):
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")
print(conta1)
#TESTE 2
print("**********TESTE 2***********")
if conta1.saque(1001):
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")
print(conta1)