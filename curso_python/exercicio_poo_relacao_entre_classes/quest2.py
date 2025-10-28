class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        print(f"O Aluno {self.nome} pegou o ônibus da linha {onibus.linha} para ir a aula.")

class Onibus:
    def __init__(self, linha):
        self.linha = linha

aluno = Aluno("Francisco")
bus = Onibus("AV. norte Macaxeira")
aluno.pegar_onibus(bus)   