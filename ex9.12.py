def contar_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        contagem = {}

        for numero_linha, linha in enumerate(linhas, start=1):

            import string
            linha_limpa = linha.translate(str.maketrans('', '', string.punctuation)).lower()

            palavras = linha_limpa.split()

            coluna_inicial = 0
            for palavra in palavras:
                coluna = linha[coluna_inicial:].lower().find(palavra) + coluna_inicial + 1
                coluna_inicial = coluna + len(palavra) - 1

                if palavra not in contagem:
                    contagem[palavra] = []
                contagem[palavra].append((numero_linha, coluna))

        return contagem

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return {}
    except Exception as e:
        print(f"Erro: {e}")
        return {}

arquivo = "texto.txt"
resultado = contar_palavras(arquivo)
print(resultado)
