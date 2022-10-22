#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cores ={'limpa':'\033[m', 'azul':'\033[36m'}
i = 0
soma = 0
##### soma += c equivale à soma=soma+c
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c #Vai somar, acumulando o valor de c(número divisível por 3), na variavel soma
        i += 1 #Vai apenas fazer a contagem de vezes em que foi encontado um número divisivel por 3
print('\nA soma de todos {}{}{} valores solicitados é {}{}{}.'.format(cores['azul'], i, cores['limpa'], cores['azul'], soma, cores['limpa']))
