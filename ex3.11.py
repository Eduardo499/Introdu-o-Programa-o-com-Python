preço = int(input('Digite o preço da mercadoria: '))
porcentagem = int(input('Digite o percentual de desconto: ')) / 100
desconto = preço * porcentagem

print(f'O valor com desconto é R$ {preço - desconto}, a mercadoria teve um desconto de R$ {desconto}')