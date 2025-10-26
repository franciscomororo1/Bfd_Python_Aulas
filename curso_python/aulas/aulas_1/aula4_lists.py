# frutas = ["banana"]
# frutas.append("manga")
# print(frutas)
#****************************************************************
#frutas.insert(1, "maracuja")
# fruta = "manga"
# print(frutas[2])
frutas = ["banana", "manga", "laranja", "jaca", "melancia", "limão", "abacaxi"]
# salada_de_frutas = frutas
# print(id(frutas))
# print(id(salada_de_frutas))
# #print(frutas[3:5])
# temperos = ["pimenta", "sal"]
#del frutas[0]
#frutas += temperos
#### REMOVER ITENS
#frutas.remove("banana")
#frutas.pop(1)
#print(frutas.clear())

#### ORDENAR LISTAS

print(sorted(frutas))
frutas.sort()
print(frutas)
frutas.sort(reverse=True)
print(frutas)

# fruta = "morango"
# morango_do_amor = fruta
# print(id(fruta))
# print(id(morango_do_amor))

#### COPIAR
#salada_de_frutas = frutas[:]

# salada_de_frutas = ["maça"]
# salada_de_frutas.extend(frutas)
# print(salada_de_frutas)

# salada_de_frutas = frutas.copy
# #salada_de_frutas = frutas[:]
# print(frutas.count("morango"))


# for fruta in frutas:
#     salada_de_frutas.append(fruta)
#     print(fruta)
#     print(salada_de_frutas)

# print(id(frutas))
# print(id(salada_de_frutas))

salada_de_frutas = ["maça"]
print(frutas)
print(frutas.index("laranja"))
idx_jaca = frutas.index("jaca")
frutas.pop(idx_jaca)
print(frutas)