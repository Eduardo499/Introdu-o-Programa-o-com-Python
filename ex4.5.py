"""
Exercício 4.5 Execute o programa (Listagem 4.5) e experimente alguns valores.
Verifique se os resultados foram os mesmos do programa anterior (Listagem 4.3).
"""

# Listagem 4.5

idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

# Listagem 4.3

idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")

# Os dois resultados são iguais.
