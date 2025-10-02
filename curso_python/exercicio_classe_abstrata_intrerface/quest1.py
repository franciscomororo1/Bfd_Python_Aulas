#Crie uma classe abstrata Pessoa que tenha os metodos: Falar, Andar e comer e subclasses funcionário e aluno, 
# que herde as características e Métodos de Pessoa. Instancie um objeto para cada subclasse.

from abc import ABC, abstractmethod

class Pessoa:
    @abstractmethod
    def falar(self):
        print("A pessoa esta falando")

    @abstractmethod
    def andar(self):
        print("A pessoa esta andando")

    @abstractmethod
    def comer(self):
        print("A pessoa esta comendo")

class Funcionario(Pessoa):
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
        
    def comer(self):
        return super().comer()
    
class Aluno(Pessoa):
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
        
    def comer(self):
        return super().comer()
    
antonio = Funcionario()
raissa = Aluno()

antonio.falar()
antonio.andar()
antonio.comer()
raissa.falar()
raissa.andar()
raissa.comer()
    


    
