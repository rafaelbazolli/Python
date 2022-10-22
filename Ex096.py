#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a, b):
    area = a * b
    print(f'A área do terreno é {area}m.')


print('_'*20)
print(' CONTROLE DE TERRENOS')
print('_'*20)

l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))

area(l, c)
