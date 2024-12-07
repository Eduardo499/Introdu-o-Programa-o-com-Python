vi = float(input('Digite o depósito inicial: '))
taxa = float(input('Digite a taxa de juros em porcentagem: ')) / 100 + 1

montante = vi
mes = 1

while mes <= 24:
    print(f'Mês {mes}')
    montante *= taxa
    print(montante)
    mes += 1
