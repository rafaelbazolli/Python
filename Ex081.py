#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    #Verificando se o usuário quer continuar ou não no programa
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'\nVocê digitou a seguinte lista: {lista}')
print(f'\nForam digitados {len(lista)} valores.')
print(f'\nA lista digitada, em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'\nO valor 5 faz parte da lista!')
else:
    print(f'\nO valor 5 não faz parte da lista!')
