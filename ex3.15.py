"""
Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

cigarros = int(input('Digite quantos cigarros foram fumados por dia: '))
anos = int(input('Digite quantos anos você fumou: '))

dias = (cigarros * 10 * anos * 365) / 60 / 24

print(f'Você perdeu {dias} dias de vida')
