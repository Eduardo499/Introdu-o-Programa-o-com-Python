último = 10
fila = list(range(1, último + 1))

while True: 
    sequencia = input('''Digite a sequência de operações
F - Adicionar novo cliente no fim da fila
A - Atender o primeiro cliente da fila
S - Sair
''')
    op = list(sequencia)

    for operacao in op:
        print(f'Existem {len(fila)} clientes na fila')
        print(f'Fila atual: {fila}')

        if operacao == 'F':
            novo_cliente = len(fila) + 1
            fila.append(novo_cliente)
            print(f'Cliente {novo_cliente} adicionado à fila.')
        elif operacao == 'A':
            if fila:
                cliente_atendido = fila.pop(0)
                print(f'Cliente {cliente_atendido} atendido e removido da fila.')
            else:
                print('Não há clientes na fila para atender.')
        elif operacao == 'S':
            print("Operação de saída detectada. Finalizando...") 
            break
        else:
            print("Operação inválida! Apenas 'F', 'A' e 'S' são permitidos.")
    if 'S' in op:
        break
