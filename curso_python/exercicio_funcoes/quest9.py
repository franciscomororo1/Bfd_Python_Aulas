def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

print(aplicar_operacao(3, 4, soma))         
print(aplicar_operacao(3, 4, multiplicacao)) 
