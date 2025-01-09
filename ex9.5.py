numeros = []

with open('pares.txt', 'r') as pares, open('pares_invertido.txt', 'w') as pares_invertido:
    for linha in pares:
        numeros.append(int(linha))
    for numero in reversed(numeros):
        pares_invertido.write(f'{str(numero)}\n')