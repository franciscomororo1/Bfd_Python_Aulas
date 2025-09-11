try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    result = n1 /n2

except ValueError:
    print("Erro: Valor digitado inválido")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero")

else:
    print(f"Resultado da divisão: {result}")

