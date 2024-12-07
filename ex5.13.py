divida = float(input('Digite sua divida: '))
taxa = float(input('Digite a taxa de juros mensal em porcentagem: ')) / 100
vm = float(input('Digite o valor mensal a ser pago: '))

valor_pago = 0
mes = 0
total_juros = 0

while divida > 0:
    mes += 1
    juros = divida * taxa
    divida += juros
    
    if divida < vm:
        vm = divida

    divida -= vm
    valor_pago += vm
    total_juros += juros

print(f'A divida será paga em {mes} meses')
print(f'O valor total pago foi de  R$ {valor_pago}')
print(f'O valor total de juros foi de R$ {total_juros}')
