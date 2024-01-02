"""
Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
"""

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
operacao = int(input("""Escolha uma operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
"""))

if operacao == 1:
    print(f'{a} + {b} = {a + b}')
elif operacao == 2:
    print(f'{a} - {b} = {a - b}')
elif operacao == 3:
    print(f'{a} X {b} = {a * b}')
elif operacao == 4:
    print(f'{a} / {b} = {a / b}')
else:
    print('Digite um número válido.')
