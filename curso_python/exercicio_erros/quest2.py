try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    result = n1 * n2
    print(f"A multiplicação de {n1} e {n2} é {result}")
except ValueError:
    print("Valor digitado não é um número")