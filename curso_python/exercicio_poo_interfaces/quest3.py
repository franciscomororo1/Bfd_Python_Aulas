from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        ...

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        ...

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("O relatório está sendo impresso.")

    def exportar(self):
        print("O relatório está sendo exportado.")

rel = Relatorio()
rel.imprimir()
rel.exportar()