import sqlite3

conexao = sqlite3.connect('curso_python/exercicio_sql_lite/escola_v2.db')

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Aluno")

resultado = cursor.fetchall()

print(resultado)

conexao.close()