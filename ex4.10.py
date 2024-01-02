quantidade = int(input('Digite a quantidade de kWh consumida: '))
tipo = int(input("""Tipos de instalação
1 - Residencial
2 - Comercial
3 - Industrial
"""))

if tipo == 1:
    if quantidade <= 500:
        print(f'O preço a pagar é R$ {quantidade * 0.40}')
    else:
        print(f'O preço a pagar é R$ {quantidade * 0.65}')
elif tipo == 2:
    if quantidade <= 1000:
        print(f'O preço a pagar é R$ {quantidade * 0.55}')
    else:
        print(f'O preço a pagar é R$ {quantidade * 0.60}')
elif tipo == 3:
    if quantidade <= 5000:
        print(f'O preço a pagar é R$ {quantidade * 0.55}')
    else:
        print(f'O preço a pagar é R$ {quantidade * 0.60}')
else:
    print('Digite uma opção válida.')