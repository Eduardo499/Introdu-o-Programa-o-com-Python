aberto = 0
fechado = 0

sequencia = input('Digite uma sequência de parênteses: ')
p = list(sequencia)

for i in p:
    if i == '(':
        aberto += 1
    elif i == ')':
        fechado += 1

if aberto == fechado:
    print('OK')
else:
    print('ERRO')
