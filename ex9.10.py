import sys

def juntar_arquivos(nomes_arquivos):
    print("Iniciando junção de arquivos...")
    try:
        with open('arquivo_final.txt', 'w') as arquivo_final:
            print("Arquivo final criado com sucesso.")
            for nome in nomes_arquivos:
                print(f"Lendo arquivo: {nome}")
                try:
                    with open(nome, 'r') as arquivo:
                        for linha in arquivo:
                            arquivo_final.write(linha)
                except FileNotFoundError:
                    print(f"Erro: O arquivo '{nome}' não foi encontrado.")
                except Exception as e:
                    print(f"Erro ao processar o arquivo '{nome}': {e}")
    except Exception as e:
        print(f"Erro ao criar o arquivo final: {e}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python ex9.10.py <arquivo1> <arquivo2> ... <arquivoN>")
        sys.exit(1)
    
    nomes_arquivos = sys.argv[1:]
    print(f"Arquivos recebidos: {nomes_arquivos}")
    juntar_arquivos(nomes_arquivos)

if __name__ == "__main__":
    main()
