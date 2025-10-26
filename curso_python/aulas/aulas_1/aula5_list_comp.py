lista1 = []

for i in range (10):
    lista1.append(i*2)

print(lista1)    


lista2 = [i for i in range(10) if i%2==0]
print(lista2)

lista3 = [[linha for linha in range(10)] for coluna in range (3)]
print(lista3)