class Televisão:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

tv_1 = Televisão('Sony', '4O"')
tv_2 = Televisão('LG', '32"')

print(tv_1.marca, tv_1.tamanho)
print(tv_2.marca, tv_2.tamanho)