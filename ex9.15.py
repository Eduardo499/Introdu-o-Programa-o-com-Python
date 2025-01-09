import random

def carregar_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return [linha.strip().lower() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []

def salvar_ranking(arquivo, ranking):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            for jogador, pontos in ranking:
                f.write(f"{jogador},{pontos}\n")
    except Exception as e:
        print(f"Erro ao salvar ranking: {e}")

def carregar_ranking(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return [linha.strip().split(',') for linha in f if linha.strip()]
    except FileNotFoundError:
        return []

def jogo_da_forca():
    palavras = carregar_palavras('palavras.txt')
    if not palavras:
        print("Nenhuma palavra disponível para o jogo.")
        return

    palavra = random.choice(palavras)
    jogador = input("Digite seu nome: ").strip()

    for _ in range(100):
        print()

    digitadas = []
    acertos = []
    erros = 0

    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "."

        print(senha)

        if senha == palavra:
            print("Você acertou!")
            break

        tentativa = input("\nDigite uma letra: ").lower().strip()

        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue
        else:
            digitadas.append(tentativa)

            if tentativa in palavra:
                acertos.append(tentativa)
            else:
                erros += 1
                print("Você errou!")

        print("X==:==\nX : ")
        print("X O " if erros >= 1 else "X")

        linha2 = ""
        if erros == 2:
            linha2 = " | "
        elif erros == 3:
            linha2 = " \| "
        elif erros >= 4:
            linha2 = " \|/ "

        print("X%s" % linha2)

        linha3 = ""
        if erros == 5:
            linha3 += " /"
        elif erros >= 6:
            linha3 += " / \ "

        print("X%s" % linha3)
        print("X\n===========")

        if erros == 6:
            print("Enforcado!")
            break

    ranking = carregar_ranking('ranking.txt')
    ranking.append((jogador, len(acertos)))
    ranking = sorted(ranking, key=lambda x: int(x[1]), reverse=True)[:5]
    salvar_ranking('ranking.txt', ranking)

    print("\nRanking atual:")
    for posicao, (nome, pontos) in enumerate(ranking, start=1):
        print(f"{posicao}. {nome} - {pontos} acertos")

jogo_da_forca()
