#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO / – Média entre 5.0 e 6.9: RECUPERAÇÃO / – Média 7.0 ou superior: APROVADO
color = {'limpa':'\033[m', 'vermelho':'\033[31m', 'azul':'\033[34m'}
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print('A média do aluno é {:.2f}'.format(media))
if media < 5:
    print('O aluno está {}REPROVADO{}.'.format(color['vermelho'], color['limpa']))
elif media >= 7:
    print('O aluno está {}APROVADO{}.'.format(color['azul'], color['limpa']))
else:
    print('O aluno está de RECUPERAÇÃO.')
