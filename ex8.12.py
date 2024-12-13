def verificar(string, lista):
    if string in lista:
        return True
    else:
        return False
    
lista = ['banana', 'melancia', 'maçã', 'pera', 'uva']
string = 'banana'

print(verificar(string, lista))
