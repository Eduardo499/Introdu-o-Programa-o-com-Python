while True:
    valor=int(input("Digite o valor a pagar (0 para sair):"))

    if valor == 0:
        break

    cédulas = 0
    apagar = valor
    atual = 50

    while apagar > 0:
        if atual<=valor:
            valor-=atual
            cédulas+=1
        else:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
            if valor == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cédulas = 0
