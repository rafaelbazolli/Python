#Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
# choice escolhe um aleatório dentro da lista
aluno = choice(lista)
print('\nO aluno escolhido foi {}.'.format(aluno))
