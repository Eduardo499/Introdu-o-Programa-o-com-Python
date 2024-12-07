vi = float(input('Digite o depósito inicial: '))
vm = float(input('Digite o valor a ser depositado mensalmente: '))
taxa = float(input('Digite a taxa de juros em porcentagem: ')) / 100 + 1

montante = vi 
mes = 0

while mes <= 23:
    print(f'Mês {mes}')
    montante *= taxa
    print(montante)
    montante += vm
    mes += 1
