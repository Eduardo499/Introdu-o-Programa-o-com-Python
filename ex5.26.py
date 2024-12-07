n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
div = 0
resto = n1

while resto >= n2:
    resto -= n2
    div += 1

print(div)

print(f'A divisão inteira de {n1} por {n2} é {div}, com resto {resto}')
