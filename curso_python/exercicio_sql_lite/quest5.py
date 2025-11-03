import sqlite3

conexao = sqlite3.connect('curso_python/exercicio_sql_lite/escola_v2.db')

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Aluno LEFT JOIN Turma ON id_turma = Turma.id WHERE Aluno.id_turma = 2")

dados = cursor.fetchall()

print("Alunos da Turma 2:\n")
for i in dados:
    print(i)

cursor.close()