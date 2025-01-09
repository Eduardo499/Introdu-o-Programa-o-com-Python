def eliminar_espacos_redundantes(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        linhas_processadas = []
        linha_em_branco = False

        for linha in linhas:
            linha_limpa = ' '.join(linha.split()).rstrip()

            if linha_limpa == '':
                if not linha_em_branco:
                    linhas_processadas.append('')
                    linha_em_branco = True
            else:
                linhas_processadas.append(linha_limpa)
                linha_em_branco = False

        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write('\n'.join(linhas_processadas) + '\n')

        print(f"Arquivo processado com sucesso. Saída salva em '{arquivo_saida}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

arquivo_entrada = "texto.txt" 
arquivo_saida = "texto_processado.txt"
eliminar_espacos_redundantes(arquivo_entrada, arquivo_saida)
