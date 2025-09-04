a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("O divisor não pode ser zero.")
    else:
        return a / b
print(dividir(a,b))