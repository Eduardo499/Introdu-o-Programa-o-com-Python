import sqlite3

produto = input('Digite o nome do produto: ').capitalize().strip()

conexão = sqlite3.connect("preços.db")

cursor = conexão.cursor()

cursor.execute("select * from precos where nome = ?", (produto,))
resultado = cursor.fetchone()

if resultado:
    print(f'{resultado[0]} custa {resultado[1]}')
else:
    print('Produto não encontrado.')

cursor.close()
conexão.close()