lista = [1,2,4,5,6,7,8,9]
p = int(input('Digite um valor para procurar na lista: '))
v = int(input('Digite o utro valor para procurar na lista: '))
x = 0

for i in lista:
    if p == i:
        print(f'{p} achado na posição {lista.index(i)}')
        x += 1
        pos_x = lista.index(i)
    elif v == i:
        print(f'{v} achado na posição {lista.index(i)}')
        pos_y = lista.index(i)
        x += 1
    
try: 
    if pos_x < pos_y:
        print(f'{p} foi encontrado primeiro')
    else:
        print(f'{v} foi encontrado primeiro')
except:
    print('Um elemento não foi encontrado')
