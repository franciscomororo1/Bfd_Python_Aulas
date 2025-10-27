from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        ...

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        ...

class Comnputador(Ligavel, Desligavel):
    def ligar(self):
        print("O computador está ligado!")

    def desligar(self):
        print("O computador está desligado!")

pc = Comnputador()
pc.ligar()
pc.desligar()