class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        self.canal = self.cmin
    def muda_canal_para_cima(self):
        self.canal = self.cmax

tv_1 = Televisão()
tv_2 = Televisão(1, 10)

print(tv_1.cmin)
print(tv_1.cmax)

print(tv_2.cmin)
print(tv_2.cmax)