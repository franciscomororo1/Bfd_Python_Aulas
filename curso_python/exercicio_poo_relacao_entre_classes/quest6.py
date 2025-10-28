class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self, endereco ):
        self.endereco = endereco
        self.comodos = [
            Comodo("Sala"),
            Comodo("Quarto"),
            Comodo("Banheiro"),
            Comodo("Cozinha")
        ]

    def listar_comodos(self):
        print(f"A casa na {self.endereco} tem os seguintes cômodos: ")
        for i in self.comodos:
            print(i.nome)

c1 = Casa("Rua Maciel Monteiro, 136")
c1.listar_comodos()