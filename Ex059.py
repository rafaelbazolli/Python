from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('==='*10)
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR 
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR ''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print()
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {:.1f} e {:.1f} é {:.1f}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = float(input('\nDigite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
sleep(2)
print('\nFim do programa. Volte Sempre!')