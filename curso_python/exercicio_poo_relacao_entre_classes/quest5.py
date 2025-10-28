class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
        print(f"O {self.modelo} tem potência no motor de {self.motor.potencia} Cavalos")

    def __del__(self):
        print(f"O {self.modelo} foi destuído e o motor dele não existe mais")

c1 = Carro("Meriva", 500)

