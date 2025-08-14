#for

alunos = fred = ["francisco", "joão", "maria", "jose"]

for aluno in alunos:
    print(aluno)

for numero in range(10):    
    print(numero)

#while

# num = 0
# while num < 10:
#     print("Dentro do while", num)
#     num += 1;

num = 0
while num < 10:
    num += 1;
    if num == 5:
        #break
        pass
    print(num)
else:
    print("sai do loop")    
    
    