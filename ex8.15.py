def imprimir_lista(L, nivel=0):

    for elemento in L:

        if isinstance(elemento, list):
            imprimir_lista(elemento, nivel + 1)
        else:
            print(' ' * nivel * 4 + str(elemento))

L = [1, [2, 3, 4, [5, 6, 7]]]
imprimir_lista(L)
