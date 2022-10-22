#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# from math import factorial
# f = factorial(num)

num = int(input('Digite um número para calcular seu fatorial: '))
i = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while i > 0 :
    print('{} '.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    fat *= i
    i -= 1
print ('{}'.format(fat))