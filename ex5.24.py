def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input('Digite um número (quantidade de números primos para exibir): '))

cont = 0
numero = 2

while cont < n:
    if verificar_primo(numero):
        print(numero)
        cont += 1
    numero += 1
