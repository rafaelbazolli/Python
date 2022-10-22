#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


num = i = soma = 0 ### todas vão receber 0
num = int(input('Digite um número[999 para parar]: '))
while num != 999:
    soma += num
    i += 1
    num = int(input('Digite um número[999 para parar]: '))
print('Você digitou {} números. A soma dos numeros digitados é {}.'.format(i, soma))
