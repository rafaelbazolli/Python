# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for i in range(0, 5):
    #Lendo os valores e guardando na lista com o append
    lista.append(int(input(f'Digite um valor inteiro para a posição {i}: ')))

    if i == 0:
        menor = maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]

print(f'\nVocê digitou os valores: {lista}')

print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
##Pegando o índice posmaior, enquanto varre a lista. Se o elemento lista, na posição posmaior, for igual ao maior, dá o print
for posmaior, mai in enumerate(lista):
    if lista[posmaior] == maior:
        print(f'{posmaior}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')

for posmenor, men in enumerate(lista):
    if lista[posmenor] == menor:
        print(f'{posmenor}...', end='')

