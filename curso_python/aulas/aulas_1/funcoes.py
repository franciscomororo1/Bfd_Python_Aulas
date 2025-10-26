# #### Exemplo Função
# def saudacao():
#     print("Oi, to entendendo nada!")

# #### Chamando a Função
# saudacao()

# ##### Informação da função Return
# def saudacao():
#     return("Oi, não estou entendendo nada!")
# print(saudacao())
# msg_duvida = saudacao()
# print(msg_duvida)

# def numero(num):
#     if num >= 4:
#         return "Maior que 4"
#     if num <= 4:
#         return "Não é maior que 4"
#     return "Olá! Tudo bem?"
# print(numero(4))

####
def soma(*nuns):
    resultado = 0
    for numero in nuns:
        resultado += numero
    return (resultado)
print(soma(2,3,5,2,7))

####

