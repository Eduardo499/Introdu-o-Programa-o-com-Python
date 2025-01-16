import sqlite3

conexão = sqlite3.connect("preços.db")

cursor = conexão.cursor()

cursor.execute("select * from precos")
resultado = cursor.fetchall()

print('Tabela de preços:')
for linha in resultado:
    print(f'{linha[0]} custa {linha[1]}')

cursor.close()
conexão.close()