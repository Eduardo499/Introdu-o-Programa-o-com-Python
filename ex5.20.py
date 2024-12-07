valor=float(input("Digite o valor a pagar:"))
cédulas=0
atual=200
apagar=valor
while apagar > 0:
    if valor < 0.01:
        print('Não existe cédula ou moeda menor que 1 centavo')
        break
    elif atual<= apagar:
        apagar-=atual
        cédulas+=1
    else:
        if cédulas > 0:
            print("%d cédula(s) de R$%.2f" % (cédulas, atual))
        cédulas = 0
        if atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
            

if cédulas > 0:
    print("%d cédula(s) de R$%.2f" % (cédulas, atual))
