from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        ...
        
class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"O Pagamento do cartão de credito no valor de {valor:.2f} foi processado com sucesso!")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"O Boleto no valor de {valor:.2f} foi gerado com sucesso!")

credito = CartaoCredito()
boleto = Boleto()
credito.processar(500)
boleto.processar(250)