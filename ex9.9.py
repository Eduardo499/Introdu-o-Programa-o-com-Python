import sys

def imprimir_arquivos(nomes_arquivos):
    for nome in nomes_arquivos:
        print(f"\n--- Conteúdo do arquivo: {nome} ---")
        try:
            with open(nome, 'r') as arquivo:
                for linha in arquivo:
                    print(linha, end="")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{nome}': {e}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python ex9.9.py <arquivo1> <arquivo2> ... <arquivoN>")
        sys.exit(1)
    
    nomes_arquivos = sys.argv[1:]
    imprimir_arquivos(nomes_arquivos)

if __name__ == "__main__":
    main()
