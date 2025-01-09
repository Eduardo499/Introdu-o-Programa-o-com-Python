def paginar_arquivo(nome_entrada, nome_saida):
    LARGURA = 76
    LINHAS_POR_PAGINA = 60 

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
            while len(linha) > LARGURA:
                saida.write(linha[:LARGURA] + '\n')
                linha = linha[LARGURA:]
                linha_atual += 1
                if linha_atual == LINHAS_POR_PAGINA:
                    saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n\n")
                    pagina_atual += 1
                    linha_atual = 0

            saida.write(linha.strip() + '\n')
            linha_atual += 1

            if linha_atual == LINHAS_POR_PAGINA:
                saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n\n")
                pagina_atual += 1
                linha_atual = 0

        if linha_atual > 0:
            saida.write(f"\n--- Página {pagina_atual} ({nome_entrada}) ---\n")

paginar_arquivo('entrada.txt', 'saida_paginada.txt')