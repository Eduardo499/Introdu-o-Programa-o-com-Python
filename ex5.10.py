pontos = 0
questão = 1
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão).capitalize()
    if questão == 1 and resposta == "B":
        pontos = pontos + 1
    if questão == 2 and resposta == "A":
        pontos = pontos + 1
    if questão == 3 and resposta == "D":
        pontos = pontos + 1
    questão +=1
print("O aluno fez %d ponto(s)" % pontos)
