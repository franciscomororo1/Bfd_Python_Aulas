from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        ...
    @abstractmethod
    def buscar(self, id):
        ...

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"O objeto {objeto} foi salvo na memória!")

# Teste com erro
# repository = RepositorioMemoria()
# repository.buscar(1)

    def buscar(self, id):
        print(f"O ID {id} foi encontrado!")

repository = RepositorioMemoria()
repository.salvar("Arquivo")
repository.buscar(50)