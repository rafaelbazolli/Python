#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*60)
print('{:^60}'.format('BANCO CEV'))
print('='*60)

valor = int(input('Qual valor você quer sacar? R$ '))

ced_inicial = 50
total = valor
qtd_ced = 0  ## vai contar quantas cédulas de cada valor vão ser dadas

while True:
    if total >= ced_inicial:  #Se o total for maior que a cédula em questão, tira o valor de 1 cédula, e continua.
        total -= ced_inicial  #E a quantidade de cédulas em questão vai aumentando de 1 em 1 pra cada vez que ele conseguir retirar
        qtd_ced += 1
    else:
        if qtd_ced >=1:
            print(f'Total de cédulas de {ced_inicial} é de {qtd_ced}')
        if ced_inicial == 50: ##Se chegou até o else, então o total faltante é menor que a céd inicial, então é necessário diminuir a cédula
            ced_inicial = 20
        elif ced_inicial == 20:
            ced_inicial = 10
        elif ced_inicial == 10:
            ced_inicial = 1
        qtd_ced = 0
        if total == 0:  #Se o total for 0, sai do laço
            break