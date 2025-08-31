palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def cont_palavras (palavras):
    contagem ={}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem
print(cont_palavras(palavras))