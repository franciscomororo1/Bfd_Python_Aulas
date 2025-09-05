def calculadora(operacao, x, y):
    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x - y
    
    def multiplicacao(x, y):
        return x * y
    
    def divisao(x, y):
        if y == 0:
            return "Erro: divisão por zero"
        return x / y
    if operacao == "somar":
        return soma(x, y)
    elif operacao == "subtrair":
        return subtracao(x, y)
    elif operacao == "multiplicar":
        return multiplicacao(x, y)
    elif operacao == "dividir":
        return divisao(x, y)
    else:
        return "Operação inválida"
    
print(f"A soma dos números é: {calculadora("somar", 5, 10)}")
print(f"A subtração dos números é: {calculadora("subtrair", 5, 10)}")
print(f"A multiplicação dos números é: {calculadora("multiplicar", 5, 10)}")
print(f"A divisão dos números é: {calculadora("dividir", 5, 10)}")