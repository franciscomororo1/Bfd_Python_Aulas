class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não poder ser negativa")
    return f"Você tem {idade} anos de idade"
    
print(cadastrar_idade(-10))
# print(cadastrar_idade(42))