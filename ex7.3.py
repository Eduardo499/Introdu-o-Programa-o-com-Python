s1 = 'CTA'
s2 = 'ABC'
lista1 = set(s1)
lista2 = set(s2)
lista3 = lista1 ^ lista2

for i in lista3:
    print(f'{i}', end='')
