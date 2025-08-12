# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print ("ele é par")
# else: 
#     print ("ele é impar")

# nota_aluno = float(input("Digite a nota do aluno:"))

# if nota_aluno < 7 and 5:
#     print ("Aluno em recuperação!")
#     if nota_aluno < 5:
#         print("Aluno reprovado")
# else:
#     print("Aluno aprovado!")
    
# for x in range(1,11):
#      print(x)

# numero = int(input("Digite um número: (de 1 a 10)"))

# print(f"Tabuada do {numero}:")
# for x in range(1,11):
#      resultado = numero * x
#      print(f"{numero} x {x} = {resultado}")

soma = 0
while True:
  numero = int(input("Digite um número (0 para sair): "))
  if numero == 0:
    break
  soma += numero

print("A soma dos números digitados é:", soma)



