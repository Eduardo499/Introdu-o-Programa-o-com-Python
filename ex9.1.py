import sys

def main():
    if len(sys.argv) < 2:
        print('Uso: python ex9.1.py <nome_do_arquivo.txt>')
        sys.exit(1)
    
    nome_arquivo = sys.argv[1]

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha, end='')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

if __name__ == "__main__":
    main()