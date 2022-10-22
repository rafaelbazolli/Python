#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

#Bibliotecas
from time import sleep

## total = total de pessoas maiores de 18 // hc = total de homens cadastrados // mm = mulheres com menos de 20 anos
total = hc = mm = 0
while True:
    print('_'*60)
    print('{:^60}'.format('CADASTRE UMA PESSOA'))
    print('_'*60)

    #Recebendo os dados
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if sexo in 'MF':
        total += 1
        #Condicionais para os incrementos em hc, mm
        if sexo == 'M':
            hc += 1
        else:
            if idade < 20:
                mm += 1

        #Recebendo a opção do usuário entre continuar ou não no programa
        print('_' * 60)
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opcao == 'N':
            break

    print('\nPor favor, digite apenas uma opção válida! Tente novamente...')
    sleep(1)

print(f'\nTotal de pessoas com mais de 18 anos: {total}\nAo todo temos {hc} homens cadastrados.\nE temos {mm} mulheres com menos de 20 anos.')
