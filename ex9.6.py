LARGURA=79

with open("entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0]==";":
            continue
        elif linha[0]==">":
            print(linha[1:].rjust(LARGURA))
        elif linha[0]=="*":
            print(linha[1:].center(LARGURA))
        elif linha[0] == "=":
            print("=" * 40)
        elif linha[0] == ".":
            input("Pressione Enter para continuar...")
        else:
            print(linha)