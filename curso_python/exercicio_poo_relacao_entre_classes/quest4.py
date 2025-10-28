class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def add_jogador(self, jogador):
        self.jogadores.append(jogador)
    
    def listar_jogadores(self):
        print(f"***Jogadores do {self.nome} ***")
        for i in self.jogadores:
            print(f"Nome: {i.nome} Posição: {i.posicao}")

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

time = Time("Santa Cruz")
j1 = Jogador("Mororó", "Atacante")
j2 = Jogador("Marcio", "Zagueiro")
j3 = Jogador("Arthur", "Zagueiro")
time.add_jogador(j1)
time.add_jogador(j2)
time.add_jogador(j3)
time.listar_jogadores()