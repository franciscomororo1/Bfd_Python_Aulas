x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

def operacoes (x, y):
    return (f"A soma de {x} + {y} = {x+y} \nA subtração de {x} - {y} = {x-y}\nA multiplicação de {x} x {y} = {x*y}")                                             

print(operacoes(x,y))