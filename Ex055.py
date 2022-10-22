#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
limpa = '\033[m'
amarelo = '\033[33m'

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1: ##Se for o primeiro número digitado, ele sempre vai ser  o maior e menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nO maior peso lido foi de  {}{}{}Kg.\nO menor peso lido foi de {}{}{}Kg.'.format(amarelo, maior, limpa, amarelo, menor, limpa))
