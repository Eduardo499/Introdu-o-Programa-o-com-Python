notas=[] 
soma=0
x=0
while x<7:
    nota = float(input(f'Nota {x + 1}: '))
    notas.append(nota)
    x += 1
x=0 
while x<7: 
    print("Nota %d: %6.2f" % (x + 1, notas[x]))
    x+=1
print("Média: %5.2f" % (sum(notas)/x))
