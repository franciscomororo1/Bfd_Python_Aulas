class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
       
    def __str__(self):
        return f"Aluno: {self.nome} Nota: {self.nota:.2f}"
class turma:
    def __init__(self):
        self.alunos = []

    def adicionar_Aluno(self, aluno):
        self.alunos.append(aluno) 
    
    def __str__(self):
      return "\n".join(str(aluno) for aluno in self.alunos)

aluno1 = Aluno("Francisco", 10)
aluno2 = Aluno("Bruna", 8.5)
aluno3 = Aluno("Brenda", 9.1) 

turma_Python = turma()
turma_Python.adicionar_Aluno(aluno1)
turma_Python.adicionar_Aluno(aluno2)
turma_Python.adicionar_Aluno(aluno3)

print(turma_Python)