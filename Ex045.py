#Crie um programa que faça o computador jogar Jokenpô com você.
cores = {'limpa':'\033[m', 'verde':'\033[32m', 'azulclaro':'\033[36m', 'roxo':'\033[35m', 'vermelho':'\033[31m'}
# Bibliotecas
from random import randint
from time import sleep

# Declaração de variáveis
itens = ('PEDRA','PAPEL','TESOURA')
comp = randint(0, 2)
e = '{}EMPATE{}'.format(cores['azulclaro'], cores['limpa'])
v = '{}JOGADOR VENCE{}'.format(cores['verde'], cores['limpa'])
d = '{}COMPUTADOR VENCE{}'.format(cores['vermelho'], cores['limpa'])
invalido = '{}JOGADA INVÁLIDA!{}'.format(cores['vermelho'], cores['limpa'])

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
opcao = int(input('Qual é a sua jogada? '))

if opcao > 2 or opcao < 0:
    print(invalido)
else:
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO\n')
    sleep(1)

#Impressão dos resultados
    print('O computador jogou {}.'.format(itens[comp]))
    print('O jogador jogou {}.'.format(itens[opcao]))

    if comp == 0: #COMPUTADOR JOGOU PEDRA
        if opcao == 0:
            print(e)
        elif opcao == 1:
            print(v)
        elif opcao == 2:
            print(d)
        else:
            print(invalido)
    elif comp == 1: #COMPUTADOR JOGOU PAPEL
        if opcao == 0:
            print(d)
        elif opcao == 1:
            print(e)
        elif opcao == 2:
            print(v)
        else:
            print(invalido)
    elif comp == 2: #COMPUTADOR JOGOU TESOURA
        if opcao == 0:
            print(v)
        elif opcao == 1:
            print(d)
        elif opcao == 2:
            print(e)
        else:
            print(invalido)