s1 = 'AAACTBF'
s2 = 'CBT'
lista1 = list(s1)
lista2 = list(s2)
lista3 = []

for i in lista1:
    for j in lista2:
        if i == j:
            lista3.append(i)

for i in lista3:
    print(f'{i}', end='')
