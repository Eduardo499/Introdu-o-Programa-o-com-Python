def validar(string, minimo, maximo):
    if minimo <= len(string) <= maximo:
        return string
    else:
        print('String fora do limite de caracteres')


minimo = int(input('Digite o valor mínimo de caracteres: '))
maximo = int(input('Digite o valor máximo de caracteres: '))
string = str(input('\n'))

validar(string, minimo, maximo)
