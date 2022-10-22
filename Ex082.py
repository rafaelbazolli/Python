#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
cont = 0
while True:
    #Recebendo os valores
    lista.append(int(input('Digite um valor: ')))

    ##Se lista na posição cont for divisível por 2, é par, então o append é na lista pares. Senão, é na lista impares
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impares.append(lista[cont])
    cont += 1

    ##Verificando se o usuário deseja continuar ou não
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'\nA lista completa de valores é: {lista}')
print(f'\nA lista de pares é: {pares}')
print(f'\nA lista de ímpares é: {impares}')