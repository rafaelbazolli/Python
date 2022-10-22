#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('=='*30)
print('{:^60}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('=='*30)

vitorias = 0
total = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor < 0:
        print('\nVocê não pode jogar um valor negativo! Tente novamente...')
        print('==' * 30)
        sleep(2)
    elif valor > 10:
        print('\nPor favor, jogue somente valores entre 0 e 10. Tente novamente...')
        print('==' * 30)
        sleep(2)
    else:
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
        pc = randint(0, 10)
        total = pc + valor
        print(f'\nVocê jogou {valor} e o computador jogou {pc}. O total deu {total}.')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR') ## Operador ternário
        if escolha == 'P':
            #Jogador escolheu par, pc é impar
            if total % 2 == 0:
                print('_' * 60)
                print('VOCÊ VENCEU! Vamos jogar novamente...')
                vitorias += 1
                sleep(1)
            else:
                print('_' * 60)
                print('VOCÊ PERDEU! \nGAME OVER')
                sleep(1)
                break
        elif escolha == 'I':
            #Jogador escolheu ímpar, pc é par
            if total % 2 == 0:
                print('_' * 60)
                print('VOCÊ PERDEU! \nGAME OVER')
                sleep(1)
                break
            else:
                print('_' * 60)
                print('VOCÊ VENCEU! Vamos jogar novamente...')
                vitorias += 1
                sleep(1)
        else:
            print('\nPor favor, selecione apenar Par ou Ímpar [P/I]!\nTente novamente...')
            sleep(2)
        print('==' * 30)
print(f'\nVocê venceu {vitorias} vezes!')