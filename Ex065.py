#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = 'S'
soma = i = media = 0

while opcao in 'Ss':
    num = float(input('Digite um número: '))
    soma += num
    i += 1
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0] ##[0] para considerar somente a primeira letra
media = soma / i
print('Você digitou {} números, e a média foi {}.\nO maior número digitado foi {}, e o menor número foi {}.'.format(i, media, maior, menor))

