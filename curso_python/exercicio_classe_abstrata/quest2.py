from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self, som):
        print(f"O animal fez {som}")

try:
    animal = Animal()
except TypeError as e:
    print("Erro: ", e)
    print("Python não permite instanciar classes abstratas com metodos não implementados")
    

