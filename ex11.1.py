import sqlite3 
conexão = sqlite3.connect("preços.db")
cursor = conexão.cursor() 
cursor.execute('''
create table precos(
nome text,
preco text)
''') 
produtos = [("Caneta", "R$ 2,00"), ("Lápis", "R$ 1,00"), ("Borracha", "R$ 0,50")]

for produto in produtos:
    cursor.execute('''
    insert into precos (nome, preco)
    values(?, ?)
    ''', produto)
conexão.commit() 
cursor.close() 
conexão.close() 