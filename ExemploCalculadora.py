import math
import os
from time import sleep

# Declaração de Variáveis 
color = {'limpa':"\033[m", 'azul':'\033[34m', 'amarelo':'\033[33m'}
space = ' '* 35
opcao = 1

# Declaração funções
def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    subtr = a - b
    return subtr

def multiplicacao(a, b):
    multip = a * b
    return multip

def divisao(a, b):
    divisao = a / b
    return divisao

def limpar():
    os.system('CLS')


# Calculadora 
while opcao != 0:
    limpar()
    print('=-' * 40, '\n{}CALCULADORA\n'.format(space), '=-' * 40)
    print('[ 1 ] SOMA \n[ 2 ] SUBTRAÇÃO\n[ 3 ] MULTIPLICAÇÃO\n[ 4 ] DIVISÃO\n\n[ 0 ] Sair')
    opcao = int(input('Selecione uma das opções: '))
    
    if opcao == 1:
        print('\nSOMA\n')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
                
        soma(num1, num2)
        sleep(10)
        
    elif opcao == 2:
        print('\nSUBTRAÇÃO\n')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        
        subtracao(num1, num2)
        sleep(10)
        
    elif opcao == 3:
        print('\nMULTIPLICAÇÃO\n')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        
        multiplicacao(num1, num2)
        sleep(10)
        
    elif opcao == 4:
        print('\nDIVISÃO\n')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        
        divisao(num1, num2)
        sleep(10)
        
    elif opcao == 0:
        break
    
    else:
        print('Por favor, digite uma opção válida!!')
        sleep(2)