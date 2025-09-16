class Computador:
    def __init__(self, modelo, processador, memoria, departamento):
        self.modelo = modelo
        self.processador = processador
        self.memoria = memoria
        
    def __str__(self):
        return f"Modelo: {self.modelo} Processador: {self.processador} Memória: {self.memoria} Derpartamento: {self.departamento}"

