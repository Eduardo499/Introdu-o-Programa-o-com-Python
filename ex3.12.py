"""
Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

distancia = int(input('Digite a distância da viagem em km: '))
velocidade = int(input('Digite a velocidade média em km/h: '))

print(f'A viagem de {distancia} km a {velocidade} km/h durará {distancia // velocidade} horas e {distancia % velocidade} minutos.')
