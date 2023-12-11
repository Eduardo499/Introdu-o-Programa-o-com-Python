"""
Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
R$ 1.200,00.
"""

salario = int(input('Digite seu salário: '))

if salario > 1200:
    print('Deve pagar imposto!')
else:
    print('Não deve pagar imposto!')
