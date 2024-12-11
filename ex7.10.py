def menu():
    continuar = 1
    while continuar:
        continuar = int(input('0 - Sair\n1 - Continuar\n'))

        if continuar:
            game()
        else:
            print('Saindo...')

def game():
    jogada = 0

    while ganhou() == 0:
        print(f'\nJogador {jogada % 2 + 1}')
        exibe()
        linha = int(input('\nLinha: '))
        coluna = int(input('\nColuna: '))

        if jogo[linha - 1][coluna - 1] == 0:
            if jogada % 2 + 1 == 1:
                jogo[linha - 1][coluna - 1] = 1
            else:
                jogo[linha - 1][coluna - 1] = -1
        else:
            print('Não está vazio')
            jogada -= 1
        
        if ganhou():
            print(f'Jogador {jogada % 2 + 1} ganhou após {jogada + 1} rodadas')

        jogada += 1


def ganhou():
    for i in range(3):
        soma = jogo[i][0] + jogo[i][1] + jogo[i][2]
        if soma == 3 or soma == -3:
            return 1
        
    for i in range(3):
        soma = jogo[0][i] + jogo[1][i] + jogo[2][i]
        if soma == 3 or soma == -3:
            return 1
    
    diagonal1 = jogo[0][0] + jogo[1][1] + jogo[2][2]
    diagonal2 = jogo[0][2] + jogo[1][1] + jogo[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1
    
    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == 0:
                print(' _ ', end=' ')
            elif jogo[i][j] == 1:
                print(' X ', end=' ')
            elif jogo[i][j] == -1:
                print(' O ', end=' ')
        print()

jogo = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

menu()
