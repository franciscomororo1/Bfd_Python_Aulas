notas = []

print("Digite as 3 notas do primeiro aluno")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
notas.append([n1,n2,n3])

print("Digite as 3 notas do segundo aluno")
av1 = float(input("Nota 1:"))
av2 = float(input("Nota 2:"))
av3 = float(input("Nota 3:"))
notas.append([av1,av2,av3])

med1 = sum(notas[0]) / 3
med2 = sum(notas[1]) / 3

print(f"A Média do Primeiro aluno é: {med1}")
print(f"A Média do Segundo aluno é: {med2}")