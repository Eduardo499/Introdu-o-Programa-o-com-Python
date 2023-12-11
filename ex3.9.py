"""
Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
"""

dias = int(input('Digite o número de dias: '))
horas = int(input('Digite o número de horas: '))
minutos = int(input('Digite o número de minutos: '))
segundos = int(input('Digite o número de segundos: '))

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(total)
