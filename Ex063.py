#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('Sequencia de Fibonacci\n', '=='*20)
termo = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
i = 3
print('{} -> {} '.format(t1, t2), end='')
while i <= termo:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print(' FIM')