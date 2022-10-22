#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    i = 0
    print('==' * 30)
    n = int(input('Gostaria de ver a tabuada de qual número? '))
    print('==' * 30)
    if n >= 0:
        while i <= 10:
            print('{} x {} = {}'.format(n, i, n*i))
            i += 1
    else:
        break
opcao = int(input('PROGRAMA TABUADA ENCERRADO!'))
