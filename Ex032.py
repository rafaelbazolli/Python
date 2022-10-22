#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
# pega a data de hoje, mas somente o ano. 
# Cálculo do ano Bissexto, o ano deve ser divisivel por 4, e não deve ser divisivel por 100. Ou, deve ser divisivel por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} é BISSEXTO.'.format(ano))
else:
    print('\nO ano {} não é BISSEXTO.'.format(ano))