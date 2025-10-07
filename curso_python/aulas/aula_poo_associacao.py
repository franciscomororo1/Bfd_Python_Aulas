class Ferramenta:
    def __init__(self, nome: str, marca: str, cor: str):
        self.nome = nome
        self.marca = marca
        self.cor = cor

class Aluno:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def anotar_atividade(self, ferramenta: Ferramenta):
        print(f"O aluno {self.nome}, esta anotando a atividade usando {ferramenta.nome} {ferramenta.marca} {ferramenta.cor}")



aluno1 = Aluno("João", 20)
caneta1 = Ferramenta("Caneta", "Pentel", "preta")
caneta2 = Ferramenta("Caneta", "Pentel", "Vermelha")

aluno1.anotar_atividade(caneta1)
aluno1.anotar_atividade(caneta2)
        