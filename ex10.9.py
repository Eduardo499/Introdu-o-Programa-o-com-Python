
class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

sp = Estado("São Paulo", "SP")
sp.cidades.append(Cidade("São Paulo", 12100000))
sp.cidades.append(Cidade("Campinas", 1500000))
sp.cidades.append(Cidade("Sorocaba", 500000))

rj = Estado("Rio de Janeiro", "RJ")
rj.cidades.append(Cidade("Rio de Janeiro", 6500000))
rj.cidades.append(Cidade("Niterói", 500000))
rj.cidades.append(Cidade("Cabo Frio", 200000))

pa = Estado("Pará", "PA")
pa.cidades.append(Cidade("Belém", 1400000))
pa.cidades.append(Cidade("Santarém", 300000))
pa.cidades.append(Cidade("Marabá", 200000))

print(f'População do Estado de São Paulo = {sum([c.populacao for c in sp.cidades])}')
print(f'População do Estado do Rio de Janeiro = {sum([c.populacao for c in rj.cidades])}')
print(f'População do Estado do Pará = {sum([c.populacao for c in pa.cidades])}')

