class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo
        self.set_saldo(saldo)
       
    def __str__(self):
        return f"Titular: {self.titular} Saldo: {self._saldo}"
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
             self.__saldo = valor
    
    def deposito(self, valor):
        self._saldo += valor
        print(f"Foi depositado {valor} reais na sua conta")

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Foi sacado {valor} reais na sua conta")
        else:
            print("Saldo insuficiente")

conta1 = ContaBancaria("Francisco", 500)
print(conta1)

conta1.deposito(100)
print("Saldo chamando getter:", conta1.get_saldo())

conta1.set_saldo(75)
print(conta1)
