import sqlite3

conexao = sqlite3.connect('curso_python/exercicio_sql_lite/escola_v2.db')

cursor = conexao.cursor()

print("Conectado ao banco com sucesso!")