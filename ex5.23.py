n = int(input('Digite um número: '))
cont = 0

for i in range(1, n + 1):
    if n % 1 == 0:
        cont += 1

if cont == 2:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')
