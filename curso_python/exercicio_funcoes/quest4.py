msg = input("Digite seu nome: ")

def mensagem (msg):
    if msg == "":
        return "Olá, visitante!"
    else:
        return msg
    
print(f"Olá {mensagem(msg)}!")