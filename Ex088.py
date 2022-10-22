#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
temp = list()
aleatorio = list()
lista = []
cont = 0

print('='*50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('='*50)

quant = int(input('Quantos jogos você quer gerar? '))
print('SORTEANDO {} JOGOS'.format(quant))
for p in range(0, quant):
    while True: ##While vai se manter até o contador atingir o valor 6, preenchendo a lista temporária com 6 números aleatórios
        num = randint(1, 60) ##Gerando números entre 1 e 60
        if num not in temp:
            temp.append(num) ##Se os números não estiverem em temp, ele adiciona em temp com o append
            cont+=1
        if cont >= 6: ## se temp já estiver com 6 elementos aleatórios, ele sai do laço
            break

    aleatorio = temp[:]
    temp.clear() ##Resetando a lista temporária
    cont = 0 ##Resetando o contador. Se ele não for resetado, ele já vai entrar no while com o cont em 6, e vai sair apenas com 1 valor aleatório
    print(f'Jogo {p+1}: {sorted(aleatorio)}')

