#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('Quem nasceu em {} completa {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos até o seu alistamento.'.format(saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
