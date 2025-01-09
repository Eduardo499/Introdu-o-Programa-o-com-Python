import sys

def main():
    if len(sys.argv) < 4:
        print('Uso: python ex9.13.py <nome_do_arquivo.txt> <linha_inicial> <linha_final>')
        sys.exit(1)
    
    nome_arquivo = sys.argv[1]
    try:
        linha_inicial = int(sys.argv[2])
        linha_final = int(sys.argv[3])
    except ValueError:
        print("Erro: As linhas inicial e final devem ser números inteiros.")
        sys.exit(1)

    if linha_inicial <= 0 or linha_final < linha_inicial:
        print("Erro: O intervalo de linhas é inválido. Verifique os valores.")
        sys.exit(1)

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                if linha_inicial <= numero_linha <= linha_final:
                    print(linha, end='')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

if __name__ == "__main__":
    main()