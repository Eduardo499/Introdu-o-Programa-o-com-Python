"""
Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h.
"""

velocidade = int(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    print('Você foi multado!')
    print(f'Você deve R$ {5 * (velocidade - 80)},00')
else:
    print('Não ultrapasse 80 km/h ou será multado.')
