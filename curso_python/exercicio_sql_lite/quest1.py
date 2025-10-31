import sqlite3

conexao = sqlite3.connect('escola_v2.db')

cursor = conexao.cursor()

print("Conectado ao banco com sucesso!")