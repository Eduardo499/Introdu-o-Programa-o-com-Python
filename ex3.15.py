cigarros = int(input('Digite quantos cigarros foram fumados por dia: '))
anos = int(input('Digite quantos anos você fumou: '))

dias = (cigarros * 10 * anos * 365) / 60 / 24

print(f'Você perdeu {dias} dias de vida')
