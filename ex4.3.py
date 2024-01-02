"""
Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

print(f'O maior número é {max(n1, n2, n3)} e o menor é {min(n1, n2, n3)}')
