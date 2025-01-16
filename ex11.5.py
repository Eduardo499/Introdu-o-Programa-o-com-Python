import sqlite3

def aumentar_preço(porcentagem):
    conexão = sqlite3.connect("preços.db")
    cursor = conexão.cursor()
    cursor.execute("select * from precos")
    resultado = cursor.fetchall()
    for linha in resultado:
        nome = linha[0]
        preco = float(linha[1].replace('R$ ', '').replace(',', '.'))
        preco *= 1 + porcentagem / 100
        cursor.execute("update precos set preco = ? where nome = ?", (f'R$ {preco:.2f}'.replace('.', ','), nome))
    conexão.commit()
    cursor.close()
    conexão.close()

aumentar_preço(10)