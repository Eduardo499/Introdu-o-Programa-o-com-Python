import os

nome = str(input('Digite o nome do arquivo ou diretório: '))

if os.path.exists(nome):
    if os.path.isdir(nome):
        print(f"O diretório '{nome}' existe.")
    elif os.path.isfile(nome):
        print(f"O arquivo '{nome}' existe.")
    else:
        print(f"'{nome}' existe, mas não é um arquivo nem um diretório padrão.")
else:
    print(f"'{nome}' não existe.")
