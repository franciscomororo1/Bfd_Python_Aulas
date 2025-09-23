class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
          
    def exibir_Informacoes(self):
        return f"Nome: {self.nome} E-mail: {self.email} "
    
    def saudacao(self):
        return "Olá, usuário"

class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario
      
    def __str__(self):
        return f"Nome: {self.nome} E-mail: {self.email} Salario: {self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email, salario)

gerente = Gerente("Francisco Mororó", "junior_mororo@hotmail.com", "8000")

print(f"Gerente: {gerente.nome}")
print(f"Email: {gerente.email}")
print(f"Salário: {gerente.salario}")