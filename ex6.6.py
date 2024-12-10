último = 10
fila = list(range(1, último + 1))
fila2 = list(range(1, último + 1))

while True: 
    sequencia = input('''Digite a sequência de operações
F - Adicionar novo cliente no fim da fila 1
A - Atender o primeiro cliente da fila 1
S - Sair
''')
    op = list(sequencia)

    for operacao in op:
        print(f'Existem {len(fila)} clientes na fila 1')
        print(f'Fila atual: {fila}')

        if operacao == 'F':
            novo_cliente = len(fila) + 1
            fila.append(novo_cliente)
            print(f'Cliente {novo_cliente} adicionado à fila 1.')
        elif operacao == 'A':
            if fila:
                cliente_atendido = fila.pop(0)
                print(f'Cliente {cliente_atendido} atendido e removido da fila 1.')
            else:
                print('Não há clientes na fila 1 para atender.')
        elif operacao == 'S':
            print("Operação de saída detectada. Finalizando...") 
            break
        else:
            print("Operação inválida! Apenas 'F', 'A' e 'S' são permitidos.")

    sequencia2 = input('''Digite a sequência de operações
G - Adicionar novo cliente no fim da fila 2
B - Atender o primeiro cliente da fila 2
S - Sair
''')
    op2 = list(sequencia2)

    for operacao in op2:
        print(f'Existem {len(fila2)} clientes na fila 2')
        print(f'Fila atual: {fila2}')

        if operacao == 'G':
            novo_cliente = len(fila2) + 1
            fila2.append(novo_cliente)
            print(f'Cliente {novo_cliente} adicionado à fila 2.')
        elif operacao == 'B':
            if fila2:
                cliente_atendido = fila2.pop(0)
                print(f'Cliente {cliente_atendido} atendido e removido da fila 2.')
            else:
                print('Não há clientes na fila 2 para atender.')
        elif operacao == 'S':
            print("Operação de saída detectada. Finalizando...") 
            break
        else:
            print("Operação inválida! Apenas 'F', 'A' e 'S' são permitidos.")
    if 'S' in op or 'S' in op2:
        break
