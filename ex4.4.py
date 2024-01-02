"""
Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%.
"""

salario = int(input('Digite o salário: '))

if salario > 1250:
    print(f'O novo salário é R$ {int(salario * 1.10)},00')
else:
    print(f'O novo salário é R$ {int(salario * 1.15)},00')
