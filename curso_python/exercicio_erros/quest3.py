try:
    numero = int(input("Digite um número inteiro: ")) 
except ValueError:
    print("O número digitado não é inteiro!")
else:
    print(f"Você digitou o número inteiro {numero}")