nota_alunos = { "Francisco" : [10, 9, 7],
                "Bruna" : [8, 7, 9],
                "Brenda" : [6, 5, 10] }

for aluno, notas in nota_alunos.items():
    soma = sum(notas)
    media = soma / 3
    print(f"A média de {aluno} é: {media:.2f}")