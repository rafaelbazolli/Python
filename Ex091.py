#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#Bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1,6)}
print('=='*15)
print('Valores Sorteados')
print('=='*15)
for k, v in jogo.items():
    ## k vai correr pelos keys, escolhendo o jogador. e vai mostrar o valor correspondente de cada jogador, pego pelo v
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=='*15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) ##Está ordenando os itens de jogo, pelo atributo 1, que é o número aleatório

for i, j in enumerate(ranking): ##como ranking é uma lista, é necessario usar o enumerate para retornar posição/valor. Se fosse um dicio, seria com o .items()
    print(f'{i+1}º lugar: {j[0]}.')
