def fibonacci(n):
    sequencia = [0, 1]

    while len(sequencia) < n:
        numero = sequencia[-1] + sequencia[-2]
        sequencia.append(numero)
    return sequencia

print(fibonacci(100))
