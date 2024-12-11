string = 'TTAAC'

frequencia = {}

for letra in string:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

for caractere, quantidade, in frequencia.items():
    print(f'{caractere}: {quantidade}x')
