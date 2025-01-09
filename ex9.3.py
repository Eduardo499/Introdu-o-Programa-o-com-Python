numeros = []

with open('impares.txt', 'w') as impares:
    for n in range(1000):
        if n % 2 != 0:
            impares.write(f'{str(n)}\n')

with open('pares.txt', 'w') as pares:
    for n in range(1000):
        if n % 2 == 0:
            pares.write(f'{str(n)}\n')

with open('impares.txt', 'r') as impares, open('pares.txt', 'r') as pares, open('pareseimpares.txt', 'w') as pareseimpares:
    for linha in impares:
        numeros.append(int(linha))
    for linha in pares:
        numeros.append(int(linha))

    for numero in sorted(numeros):
        pareseimpares.write(f'{str(numero)}\n')
