def contar_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            texto = f.read()

        import string
        texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()

        palavras = texto.split()

        contagem = {}
        for palavra in palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1

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
