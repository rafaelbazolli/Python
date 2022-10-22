# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
azul = '\033[36m'
limpa = '\033[m'
vermelho = '\033[31m'

num = int(input('Digite um número: '))
i = 0
for c in range(1, num+1):
    if num % c == 0: #### Vai validar se o número digitado, é divisível por todos dentro do range
        print('{}'.format(azul), end='') ##Sempre que o resto for zero, muda a cor do número exposto para azul
        i += 1 ###Contador para verificar quantas vezes ele foi divisível por outro número
    else:
        print('{}'.format(limpa), end='')
    print('{} '.format(c), end='')
if i == 2: ###Só é um numero primo se for divisivel por 1 e por ele mesmo, ou seja, no máximo por 2 números.
    print('\n{}O número {} É PRIMO.'.format(limpa, num))
else:
    print('\n{}O número {} {}NÃO É PRIMO{}.'.format(limpa, num, vermelho, limpa))
