import sqlite3

conexao = sqlite3.connect('curso_python/exercicio_sql_lite/escola_v2.db')

cursor = conexao.cursor()

cursor.execute("SELECT nome, (nota1 + nota2) / 2 AS media FROM Aluno ORDER BY media DESC LIMIT 10")

top10 = cursor.fetchall()

print("10 Melhores médias entre os alunos:\n")

for nome, media in top10:
    print(f"Aluno: {nome} Média: {media:.2f}")

conexao.close()