b = 2
n = int(input('Digite um número para calcular sua raiz quadrada: '))
p = (b + (n / b)) / 2

while abs(n - p * p) > 0.0001:
    b = p
    p = (b + (n / b)) / 2

print(p)
