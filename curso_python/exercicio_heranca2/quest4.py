class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
          
    def exibir_Informacoes(self):
        return f"Nome: {self.nome} E-mail: {self.email} "
    
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente"
    
    def __str__(self):
        return f"Nome: {self.nome} E-mail: {self.email} Saldo: {self.saldo}"

cliente1 = Cliente("Francisco Mororó", "junior_mororo@hotmail.com", 5000)

print(cliente1)
