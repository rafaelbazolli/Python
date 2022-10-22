#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
limpa = '\033[m'
amarelo = '\033[33m'

from datetime import date
i = 0
j = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = date.today().year - ano
    if idade >=18:
        i += 1
    else:
        j += 1
print('Ao todos tiveram {}{}{} pessoas maiores de idade.\nE também tivemos {}{}{} pessoas menores de idade.'.format(amarelo,i, limpa, amarelo, j, limpa))
