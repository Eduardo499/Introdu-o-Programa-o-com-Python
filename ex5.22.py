while True:
    op = int(input("""Escolha uma opção
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Saída
"""))
    if op == 1:
        i = 1
        n = int(input('Digite um número para calcular sua tabuada: '))
        fim = int(input('Digite o número final: '))
        while i <= fim:
            print(f'{n} + {i} = {n + i}')
            i += 1
    elif op == 2:
        i = 1
        n = int(input('Digite um número para calcular sua tabuada: '))
        fim = int(input('Digite o número final: '))
        while i <= fim:
            print(f'{n} - {i} = {n - i}')
            i += 1
    elif op == 3:
        i = 1
        n = int(input('Digite um número para calcular sua tabuada: '))
        fim = int(input('Digite o número final: '))
        while i <= fim:
            print(f'{n} / {i} = {n / i}')
            i += 1
    elif op == 4:
        i = 1
        n = int(input('Digite um número para calcular sua tabuada: '))
        fim = int(input('Digite o número final: '))
        while i <= fim:
            print(f'{n} x {i} = {n * i}')
            i += 1
    elif op == 5:
        break
    else:
        print('Opção inválida.')
