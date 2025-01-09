import sys

def paginar_arquivo(nome_entrada, nome_saida, largura, linhas_por_pagina):
    try:
        with open(nome_entrada, 'r') as entrada:
            linhas = entrada.readlines()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_entrada}' não foi encontrado.")
        return

    pagina_atual = 1
    linha_atual = 0

    with open(nome_saida, 'w') as saida:
        for linha in linhas:
            while len(linha) > largura:
                saida.write(linha[:largura] + '\n')
                linha = linha[largura:]
                linha_atual += 1
                if linha_atual == linhas_por_pagina:
                    saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n\n")
                    pagina_atual += 1
                    linha_atual = 0

            saida.write(linha.strip() + '\n')
            linha_atual += 1

            if linha_atual == linhas_por_pagina:
                saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n\n")
                pagina_atual += 1
                linha_atual = 0

        if linha_atual > 0:
            saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n")

def main():
    if len(sys.argv) != 5:
        print("Uso: python script.py <arquivo_entrada> <arquivo_saida> <largura_linha> <linhas_por_pagina>")
        sys.exit(1)

    nome_entrada = sys.argv[1]
    nome_saida = sys.argv[2]
    try:
        largura = int(sys.argv[3])
        linhas_por_pagina = int(sys.argv[4])
    except ValueError:
        print("Erro: A largura da linha e o número de linhas por página devem ser números inteiros.")
        sys.exit(1)

    paginar_arquivo(nome_entrada, nome_saida, largura, linhas_por_pagina)

if __name__ == "__main__":
    main()
