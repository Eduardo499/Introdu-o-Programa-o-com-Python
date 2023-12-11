"""
Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.
"""

km = int(input('Digite quantos quilometros foram percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi utilizado: '))

print(f'Você deve pagar {dias * 60 + 0.15 * km}')
