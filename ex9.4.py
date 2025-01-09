import sys

def main():
    if len(sys.argv) < 3:
        print('Uso: python ex9.4.py <arquivo_um.txt> <arquivo_dois.txt>')
        sys.exit(1)
    
    arquivo_um = sys.argv[1]
    arquivo_dois = sys.argv[2]

    try:
        with open(arquivo_um, 'r') as arquivo_1, open(arquivo_dois, 'r') as arquivo_2, open('arquivo_tres.txt', 'w') as arquivo_3:
            for linha in arquivo_1:
                arquivo_3.write(linha)
            for linha in arquivo_2:
                arquivo_3.write(linha)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_um}' e/ou '{arquivo_dois}' não foram encontrados.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
