distancia = int(input('Digite a distância da viagem em km: '))
velocidade = int(input('Digite a velocidade média em km/h: '))

print(f'A viagem de {distancia} km a {velocidade} km/h durará {distancia // velocidade} horas e {distancia % velocidade} minutos.')
