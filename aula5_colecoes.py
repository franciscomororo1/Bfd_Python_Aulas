#### TUPLAS
# tupla1 = (1,2,3,4)

# for num in tupla1:
#     print(num+5)
# print(type(tupla1))

# tupla2 = ("Fred", "João", "Maria")

# print(tupla2.count("fred"))

#### Conjunto set

# teste = {"Fred", "Fred"}
# print(type(teste))

# teste= {1,2}
# teste.add(4)
# teste2 = teste.copy
# print(teste2)
# print(teste)

frutas = {"banana", "limão", "tomate"}
legumes = {"cenoura", "tomate", "beterraba"}
#print(legumes.difference(frutas))
#print(legumes.difference_update(frutas))
#print(legumes)
print(legumes.intersection(frutas))
print(legumes | frutas)

#### DICIONARIO

lista_alunos {"nome":"Fred",
             "Idade" : 36,
             "Endereço" : "Rua x",
             "Turma" : ("turma 34", "Turma 36")}