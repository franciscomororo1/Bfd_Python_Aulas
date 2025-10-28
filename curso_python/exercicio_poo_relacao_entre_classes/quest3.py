class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def add_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionario(self):
        print(f"Funcionario do Derpartamento de {self.nome}")
        for i in self.funcionarios:
          print(f"Nome: {i.nome} Cargo: {i.cargo}")

func1 = Funcionario("Francisco", "Analista de Suporte Técnico III")
func2 = Funcionario("Ester", "Analista de Monitoramento")

dep = Departamento("Tecnologia da Informação")
dep.add_funcionario(func1)
dep.add_funcionario(func2)
dep.listar_funcionario()