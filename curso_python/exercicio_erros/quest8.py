try:
    n1 = int(input("Digite um número: "))

except ValueError:
    print("Erro: Digite um número inteiro")

else:
    if n1 % 2 == 0:
        print(f"{n1} é par")
    else:
        print(f"{n1} é ímpar")
finally:
    print("Programa finalizado")