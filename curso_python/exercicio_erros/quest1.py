try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número inteiro {numero}")
except ValueError:
    print("O número digitado não é inteiro!")

