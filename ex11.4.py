import sqlite3

conexão = sqlite3.connect("preços.db")

valor1 = float(input('Digite o valor de um produto: '))
valor2 = float(input('Digite o valor de outro produto: '))

valor1 = 'R$ ' + str(valor1).replace('.', ',') + '0'
valor2 = 'R$ ' + str(valor2).replace('.', ',') + '0'

cursor = conexão.cursor()
cursor.execute("select * from precos where preco = ? or preco = ?", (valor1, valor2))
resultado = cursor.fetchall()

if resultado:
    for linha in resultado:
        print(f'{linha[0]} custa {linha[1]}')
else:
    print('Produto não encontrado.')

cursor.close()
conexão.close()