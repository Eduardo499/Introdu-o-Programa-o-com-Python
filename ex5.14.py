soma = 0
cont = 0

while True:
    n = int(input('Digite um número (0 para parar): '))
    if n == 0:
        break
    soma += n
    cont += 1

print(f'Foram digitados {cont} números, sua soma dos números digitados é {soma}; sua média é {soma / cont}')
