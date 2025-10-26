from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self, som):
        print(f"O animal fez {som}")

class Gato (Animal):
    def falar(self, som):
        return super().falar(som)
    
class Vaca (Animal):
    def falar(self, som):
        return super().falar(som)
    
gato = Gato()
vaca = Vaca()
gato.falar("Miau")
vaca.falar("Muuu")

