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
            print(f"Foi sacado {valor} reais na sua conta")
        else:
            print("Saldo insuficiente")

conta1 = ContaBancaria("Rodolfo", 10)
print(conta1)
conta1.deposito(50000)
print(conta1)
conta1.saque(60000)
conta1.saque(5000)
print(conta1)