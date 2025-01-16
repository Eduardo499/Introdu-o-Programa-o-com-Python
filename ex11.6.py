import sqlite3

def alterar_preço(produto, preço):
    conexão = sqlite3.connect("preços.db")
    cursor = conexão.cursor()
    cursor.execute("update precos set preco = ? where nome = ?", (preço, produto))
    conexão.commit()
    cursor.close()
    conexão.close()

produto = input('Digite o nome do produto: ').capitalize().strip()
preço = input('Digite o novo preço do produto: ').strip()

alterar_preço(produto, preço)