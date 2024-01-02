"""
Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.
"""

casa = int(input('Diigte o valor do imóvel: '))
salario = int(input('Digite o valor de seu salário: '))
parcelas = int(input('Digite com quantas parcelas você deseja pagar: '))
prestacao = casa / parcelas

if prestacao > salario * 0.3:
    print('Infelizmente você não pode comprar esse imóvel com essa quantidade de parcelas')
    print(f'A quantidade mínima de parcelas deve ser {int(casa / (salario * 0.30)) + 1}')
else:
    print(f'As parcelas ficam R$ {prestacao:.2f}')
