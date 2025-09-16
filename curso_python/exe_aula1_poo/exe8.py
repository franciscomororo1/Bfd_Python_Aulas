class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
       
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota:.2f}"

aluno1 = Aluno("Francisco", 10)
aluno2 = Aluno("Bruna", 8.5)
aluno3 = Aluno("Brenda", 9.1)

print(aluno1)
print(aluno2)
print(aluno3)