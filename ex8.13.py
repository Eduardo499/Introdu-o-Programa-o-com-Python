import random

erro = 0
acerto = 0

while True:
    n = random.randint(1,10)
    x = int(input("Escolha um número entre 1 e 10: "))

    if x == n:
        print("Você acertou!")
        acerto += 1
    else:
        print("Você errou.")
        erro += 1

    if acerto == 3:
        print('Você ganhou!')
        break
    elif erro == 3:
        print('Você perdeu!')
        break
