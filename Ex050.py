#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
i = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:
        soma += num
        i += 1
if soma == 0:
    print('\nNão foi encontrado nenhum número par entre os valores fornecidos.')
else:
    print('\nVocê informou {} números pares. A soma dos números pares encontrados foi: {}'.format(i, soma))
