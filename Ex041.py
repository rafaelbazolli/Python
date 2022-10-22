#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM / – Até 14 anos: INFANTIL / – Até 19 anos: JÚNIOR / – Até 25 anos: SÊNIOR / – Acima de 25 anos: MASTER
color = {'limpa':"\033[m", 'azul':'\033[34m'}
from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('\nO atleta tem {} anos.\n'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}.'.format(color['azul'], color['limpa']))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}.'.format(color['azul'], color['limpa']))
elif idade <= 19:
    print('Classificação: {}JÚNIOR{}.'.format(color['azul'], color['limpa']))
elif idade <= 25:
    print('Classificação: {}SÊNIOR{}.'.format(color['azul'], color['limpa']))
else:
    print('Classificação: {}MASTER{}.'.format(color['azul'], color['limpa']))
