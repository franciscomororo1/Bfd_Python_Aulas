class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}"

carro1 = Carro("Chevrolet", "Meriva", 2012)
print(carro1)

carro1.ano = 2009
print(carro1)