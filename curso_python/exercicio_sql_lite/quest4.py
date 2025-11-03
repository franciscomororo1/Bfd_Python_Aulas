import sqlite3

conexao = sqlite3.connect('curso_python/exercicio_sql_lite/escola_v2.db')

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Aluno LEFT JOIN Turma ON id_turma = Turma.id")

dados = cursor.fetchall()

print("Combinação dos dados de Aluno e Turma:\n")
for i in dados:
    print(i)

cursor.close()