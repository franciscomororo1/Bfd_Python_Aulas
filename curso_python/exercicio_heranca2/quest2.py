class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
          
    def exibir_Informacoes(self):
        return f"Nome: {self.nome} E-mail: {self.email} "

class Cliente(Usuario):
    ...

cliente1 = Cliente("Francisco Mororó", "junior_mororo@hotmail.com")

print(cliente1.exibir_Informacoes())