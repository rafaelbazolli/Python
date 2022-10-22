from random import randint
from time import sleep
# gerando o número aleatório entre 0 e 5
computador = randint(0, 5)
print('-=-'*30)
print('Pensei em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
numero = int(input('Qual número você acha que eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
# comando sleep vai aguardar (em segundos) o tempo para executar a proxima ação
sleep(3)
print('O numero que você digitou foi {}.'.format(numero))
if numero == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, numero))
