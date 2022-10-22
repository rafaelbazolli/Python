#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

#Bibliotecas
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end=' ')
for n in tupla:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(tupla)}')  ##max pega o maior valor dentro da tupla
print(f'\nO menor valor sorteado foi {min(tupla)}')  ##min pega o menor valor dentro da tupla