salario = int(input('Digite o salário: '))
porcentagem = int(input('Digite a porcentagem de aumento: ')) / 100
aumento = salario * porcentagem

print(f'Seu novo salário é R$ {salario + aumento}, aumentou R$ {aumento}')
