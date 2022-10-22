#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

#Bibliotecas
from time import sleep

print('-'*60)
print('{:^60}'.format('LOJA SUPER BARATÃO'))
print('-'*60)

#Declarando as variaveis
## total = total da compra // cprod = produtos custando mais de R$ 1000,00
total = cprod = cont = 0

while True:

    #Recebendo os valores
    prod = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1

    #Condicionais para os incrementos
    if preco > 1000:
        cprod += 1
    if cont == 1:
        precom = preco
        produtob = prod
    if preco < precom:
        precom = preco
        produtob = prod
    total += preco

    opcao = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('-' * 60)
print(f'\nO total da compra foi R$ {total:.2f}.\nTemos {cprod} produtos custando mais de R$ 1000,00.\nO produto mais barato foi {produtob}, que custa R$ {precom:.2f}.')