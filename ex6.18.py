frase = str(input('Digite uma frase: ')).strip()
caracteres =  []
dicionario = {}

for letra in frase:
    if letra == ' ':
        pass
    else:
        caracteres.append(letra)

for letra in caracteres:
    dicionario[letra] = caracteres.count(letra)         

print(caracteres)
print(dicionario)
