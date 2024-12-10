lista = [1,2,4,5,6,7,8,9]
p = int(input('Digite um valor para procurar na lista: '))
x = 0

for i in lista:
    if p == i:
        print(f'{p} achado na posição {lista.index(i)}')
        x += 1

if x == 0:
    print('Elemento não encontrado')
