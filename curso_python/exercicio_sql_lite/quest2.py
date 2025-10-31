import sqlite3

conexao = sqlite3.connect('escola_v2.db')

cursor = conexao.cursor()

cursor.execute("""SELECT * FROM Aluno""")

print(cursor.execute.fetchall())

