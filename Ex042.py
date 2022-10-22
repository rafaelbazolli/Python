#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais / – ISÓSCELES: dois lados iguais, um diferente / – ESCALENO: todos os lados diferentes
color = {'limpa':"\033[m", 'azul':'\033[34m'}

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1+ r2:
    print('\nOs segmentos acima PODEM FORMAR um triângulo.')
    if r1 == r2 == r3:
        print('{}EQUILÁTERO{}.'.format(color['azul'], color['limpa']))
    elif r1 != r2 != r3 != r1:
        print('{}ESCALENO{}.'.format(color['azul'], color['limpa']))
    else:
        print('{}ISÓSCELES{}.'.format(color['azul'], color['limpa']))
else:
    print('\nOs segmentos acima NÃO PODEM formar um triângulo.')