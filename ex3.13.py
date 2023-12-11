"""
Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é: F = 9 X C / 5 + 32
"""

c = int(input('Digite uma temperatura em °C: '))
f = c * 9 / 5 + 32

print(f'A temperatura °C {c} convertida fica °F {f}')
