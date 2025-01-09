agenda = []
agenda_alterada = False

def pede_nome():
    return input("Nome: ")

def pede_telefone():
    return input("Telefone: ")

def mostra_dados(nome, telefone):
    print("Nome: %s Telefone: %s" % (nome, telefone))

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def salva_nome_arquivo(nome_arquivo):
    with open("ultimo_arquivo.txt", "w", encoding="utf-8") as arquivo_controle:
        arquivo_controle.write(nome_arquivo)

def le_nome_arquivo():
    try:
        with open("ultimo_arquivo.txt", "r", encoding="utf-8") as arquivo_controle:
            return arquivo_controle.read().strip()
    except FileNotFoundError:
        return None

def novo():
    global agenda, agenda_alterada
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    agenda_alterada = True 

def apaga():
    global agenda, agenda_alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        confirmacao = input(f"Você tem certeza que deseja excluir o contato '{nome}'? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            del agenda[p]
            agenda_alterada = True 
            print(f"Contato '{nome}' excluído com sucesso.")
        else:
            print("Exclusão cancelada.")
    else:
        print("Nome não encontrado.")

def altera():
    global agenda, agenda_alterada
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)

        confirmacao = input(f"Você tem certeza que deseja alterar o contato '{nome}'? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
            agenda_alterada = True 
            print(f"Contato '{nome}' alterado com sucesso.")
        else:
            print("Alteração cancelada.")
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n------")
    for i, e in enumerate(agenda):
        print("Posição: %d" % i)
        mostra_dados(e[0], e[1])
    print("------\n")

def grava():
    global agenda, agenda_alterada
    if agenda_alterada:
        nome_arquivo = pede_nome_arquivo()
        arquivo = open(nome_arquivo, "w", encoding="utf-8")
        for e in agenda:
            nome = e[0].replace("#", "\\#")
            telefone = e[1].replace("#", "\\#")
            arquivo.write("%s#%s\n" % (nome, telefone))
        arquivo.close()
        salva_nome_arquivo(nome_arquivo)
        agenda_alterada = False
        print("Agenda gravada com sucesso.")
    else:
        print("A agenda não foi alterada. Nenhuma gravação necessária.")

def lê():
    global agenda, agenda_alterada
    nome_arquivo = le_nome_arquivo()
    if nome_arquivo:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split("#")
            nome = nome.replace("\\#", "#")
            telefone = telefone.replace("\\#", "#")
            agenda.append([nome, telefone])
        arquivo.close()
        agenda_alterada = False
        print(f"Agenda carregada do arquivo '{nome_arquivo}'.")
    else:
        print("Nenhum arquivo de agenda encontrado.")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def ordena():
    global agenda
    agenda.sort(key=lambda x: x[0].lower())

def menu():
    print("""
Agenda - Contatos: %d

1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""" % len(agenda))
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

lê()

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordena()
