class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Erro: Saldo Insuficiente")
    return f"Seu novo saldo é: {saldo - valor:.2f}"

try:
    saldo_atual = 1000
    valor_saque = float(input("Digite um valor para saque: "))
    novo_saldo = sacar(saldo_atual, valor_saque)

except ValueError:
    print("Erro: Você deve digitar um número válido.")

except SaldoInsuficienteError as e:
    print(e)

else:
    print(f"Saque realizado com sucesso! {novo_saldo}")