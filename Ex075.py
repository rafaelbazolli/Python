#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na posição {n.index(3)+1}ª posição.')
print(f'Os valores pares digitados foram: ', end=' ')
for i in n:
    if i % 2 == 0:
        print(f'{i}', end=' ')
