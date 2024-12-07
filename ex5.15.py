total = 0

while True:
    cod = int(input('Digite o código (0 para parar): '))
    
    if cod == 0:
        break
    elif cod == 1:
        qtd = int(input('Digite a quantidade: '))
        total += 0.5 * qtd
    elif cod == 2:
        qtd = int(input('Digite a quantidade: '))
        total += 1 * qtd
    elif cod == 3:
        qtd = int(input('Digite a quantidade: '))
        total += 4 * qtd
    elif cod == 5:
        qtd = int(input('Digite a quantidade: '))
        total += 7 * qtd
    elif cod == 9:
        qtd = int(input('Digite a quantidade: '))
        total += 8 * qtd
    else:
        print('Código inválido.')

print(f'O total foi R$ {total}')
