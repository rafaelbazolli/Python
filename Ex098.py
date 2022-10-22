#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 // b) de 10 até 0, de 2 em 2 // c) uma contagem personalizada

from time import sleep

def contador(i, f, p): #Inicio, fim, passo
    # O passo não pode ser negativo.
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #Se o início for menor que o fim, ele faz a contagem normalmente
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) ##flush True desliga o buffer de tela, permitindo que o sleep funcione corretamente
            cont+= 1
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= 1
            sleep(0.5)
        print('FIM!')
    print('-='*20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
