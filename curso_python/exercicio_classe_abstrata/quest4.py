from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "O carro está em movimento"

# try:
#     carro = Carro()
# except TypeError as e:
#     print("Erro:", e)
#     print("Como o metodo parar ainda não foi implementado a classe Carro ainda é abstrata")

    def parar(self):
        return "O Carro está parado"
    
carro = Carro()
print(carro.mover())
print(carro.parar())


