#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    #Recebendo o valor
    num = (int(input('Digite um valor: ')))

    #Só vai atribuir à lista se o valor num não estiver na lista, evitando assim as repetições
    if num not in lista:
        lista.append(num)

    #Validando a opção de continuar ou não no programa
    opcao = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'\nVocê digitou os valores {sorted(lista)}')