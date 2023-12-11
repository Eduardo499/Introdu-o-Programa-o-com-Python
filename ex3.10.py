"""
Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.
"""

salario = int(input('Digite o salário: '))
porcentagem = int(input('Digite a porcentagem de aumento: ')) / 100
aumento = salario * porcentagem

print(f'Seu novo salário é R$ {salario + aumento}, aumentou R$ {aumento}')
