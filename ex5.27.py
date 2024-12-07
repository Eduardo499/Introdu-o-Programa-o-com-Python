n  = str(input('Digite um número: '))
numero = [digito for digito in n]

n2 = ''.join(numero[::-1])

if n == n2:
    print(f'{n} é um palíndromo.')
else:
    print(f'{n} não é um palíndromo.')
