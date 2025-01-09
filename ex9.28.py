agenda = []
agenda_alterada = False

def pede_nome():
    return input("Nome: ")

def pede_telefone():
    return input("Telefone: ")

def pede_tipo_telefone():
    tipos = ["Celular", "Fixo", "Residência", "Trabalho", "Fax"]
    print("Tipos de telefone disponíveis:")
    for i, tipo in enumerate(tipos, 1):
        print(f"{i} - {tipo}")
    while True:
        try:
            escolha = int(input("Escolha o tipo de telefone (1 a 5): "))
            if 1 <= escolha <= 5:
                return tipos[escolha - 1]
        except ValueError:
            pass
        print("Escolha inválida. Tente novamente.")

def pede_aniversario():
    return input("Data de Aniversário (DD/MM/AAAA): ")

def pede_email():
    return input("E-mail: ")

def mostra_dados(nome, telefones, aniversario, email):
    telefones_str = ", ".join([f"{t['tipo']}: {t['numero']}" for t in telefones])
    print(f"Nome: {nome} | Telefones: {telefones_str} | Aniversário: {aniversario} | E-mail: {email}")

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def nome_repetido(nome):
    for contato in agenda:
        if contato[0].lower() == nome.lower(): 
            return True
    return False

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
    if nome_repetido(nome):
        print("Erro: Nome já existe na agenda.")
        return
    telefone = pede_telefone()
    tipo_telefone = pede_tipo_telefone()
    aniversario = pede_aniversario()
    email = pede_email()
    agenda.append([nome, [{"numero": telefone, "tipo": tipo_telefone}], aniversario, email])
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
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        nome_antigo, telefones, aniversario, email = agenda[p]
        print("Encontrado:")
        mostra_dados(nome_antigo, telefones, aniversario, email)

        confirmacao = input(f"Você tem certeza que deseja alterar o contato '{nome_antigo}'? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            nome = pede_nome()
            telefones = []
            while True:
                telefone = pede_telefone()
                tipo_telefone = pede_tipo_telefone()
                telefones.append({"numero": telefone, "tipo": tipo_telefone})
                mais_telefones = input("Deseja adicionar outro telefone? (sim/não): ").strip().lower()
                if mais_telefones != "sim":
                    break
            aniversario = pede_aniversario()
            email = pede_email()
            agenda[p] = [nome, telefones, aniversario, email]
            agenda_alterada = True 
            print(f"Contato '{nome}' alterado com sucesso.")
        else:
            print("Alteração cancelada.")
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1], e[2], e[3])
    print("------\n")

def grava():
    global agenda, agenda_alterada
    if agenda_alterada: 
        nome_arquivo = pede_nome_arquivo()
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                nome = e[0].replace("#", "\\#")
                telefones = e[1]
                aniversario = e[2].replace("#", "\\#")
                email = e[3].replace("#", "\\#")
                telefones_str = "#".join([f"{t['numero']}|{t['tipo']}" for t in telefones])
                arquivo.write(f"{nome}#{telefones_str}#{aniversario}#{email}\n")
        salva_nome_arquivo(nome_arquivo) 
        agenda_alterada = False 
        print("Agenda gravada com sucesso.")
    else:
        print("A agenda não foi alterada. Nenhuma gravação necessária.")

def lê():
    global agenda, agenda_alterada
    try:
        nome_arquivo = le_nome_arquivo() 
        if nome_arquivo:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                agenda = []
                for l in arquivo.readlines():
                    campos = l.strip().split("#")
                    nome = campos[0]
                    telefones = []
                    for telefone_str in campos[1].split("|"):
                        numero, tipo = telefone_str.split("|")
                        telefones.append({"numero": numero, "tipo": tipo})
                    aniversario = campos[2]
                    email = campos[3]
                    agenda.append([nome, telefones, aniversario, email])
            agenda_alterada = False 
            print(f"Agenda carregada do arquivo '{nome_arquivo}'.")
        else:
            print("Nenhum arquivo de agenda encontrado.")
    except (IOError, OSError) as e:
        print(f"Erro ao ler a agenda: {e}")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def ordena():
    global agenda
    agenda.sort(key=lambda x: x[0].lower())

def menu():
    print(f"""
Agenda - Contatos: {len(agenda)}

1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
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
