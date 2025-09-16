class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf
        self._identidade = identidade 
       
    def __str__(self):
        return f"Nome: {self.nome} Nascimento: {self.data_nascimento} CPF: {self._cpf} RG: {self._identidade}"
    
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, digito):
        self._cpf = digito
    
    def get_identidade(self):
        return self._identidade
    
    def set_identidade(self, rg):
        self._identidade = rg

pessoa1 = Pessoa("Francisco", "11/07/1983", 12345678946, 2435678)
print(pessoa1)
pessoa1.get_cpf()
pessoa1.set_cpf(12345678990)
print(pessoa1)
pessoa1.get_identidade()
pessoa1.set_identidade(19876543)
print(pessoa1)