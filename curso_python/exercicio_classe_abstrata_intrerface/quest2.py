from abc import ABC, abstractmethod

class Pessoa:
    @abstractmethod
    def falar(self):
        ...

    @abstractmethod
    def andar(self):
        ...

    @abstractmethod
    def comer(self):
        ...

class Funcionario(Pessoa):
    def falar(self, palavras):
        print(f"O funcionário falou {palavras} palavras.")
    
    def andar(self, caminhando):
        print(f"O funcionário está caminhando {caminhando} metros.")
    
        
    def comer(self, comida):
        print(f"O funcionário está comendo {comida}.")
    
class Aluno(Pessoa):
    def falar(self, palavras):
        print(f"O aluno falou {palavras} palavras.")
    
    def andar(self, caminhando):
        print(f"O aluno está caminhando {caminhando} metros.")
        
    def comer(self, comida):
        print(f"O funcionário está comendo {comida}.")
    
antonio = Funcionario()
raissa = Aluno()

antonio.falar(200)
antonio.andar(300)
antonio.comer("banana")
raissa.falar(150)
raissa.andar(250)
raissa.comer("Maçã")